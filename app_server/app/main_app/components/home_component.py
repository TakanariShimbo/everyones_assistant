from textwrap import dedent
from typing import Optional, Literal

import streamlit as st
from streamlit_lottie import st_lottie_spinner

from ...base import BaseComponent
from .. import s_states as SStates
from .sign_in_pre_component import SignInPreComponent
from .chat_room_pre_component import ChatRoomPreComponent
from .account_pre_component import AccountPreComponent
from .home_action_results import CreateActionResults, EnterActionResults, RoomContainerActionResults
from model import ChatRoomDto, RELEASE_TYPE_TABLE, LoadedLottie, LoadedImage


class HomeComponent(BaseComponent):
    @staticmethod
    def init() -> None:
        SStates.CurrentComponentEntity.init()
        SStates.SignedInAccountEntity.validate()
        SStates.CreateChatRoomProcess.init()
        SStates.EnterChatRoomProcess.init()
        SStates.LoadedMainHomeManager.validate()
        SignInPreComponent.init()
        ChatRoomPreComponent.init()
        AccountPreComponent.init()

    @staticmethod
    def _display_titles() -> None:
        current_component_entity = SStates.CurrentComponentEntity.get()
        st.markdown(f"### {current_component_entity.label_en}")

    @classmethod
    def _display_sidebar_titles(cls) -> None:
        st.sidebar.image(image=LoadedImage.LOGO, use_column_width=True)
        st.sidebar.button(label="🚪 Sign out", key="SignOutButton", on_click=cls._on_click_sign_out, use_container_width=True)
        st.sidebar.markdown("## Menus")
        st.sidebar.button(label="👤 Account", key="AccountsButton", on_click=cls._on_click_accounts, use_container_width=True)

    @staticmethod
    def _display_overview() -> None:
        st.markdown("#### 🔎 Overview")
        with st.container(border=True):
            content = dedent(
                f"""
                Welcome to Everyone's Assistant.   
                Experience the forefront of AI technology and explore the possibilities of the future.  
                AI makes your daily life smarter and easier.  
                """
            )
            st.markdown(content)

    @staticmethod
    def _display_create_form_and_get_results() -> CreateActionResults:
        st.markdown("#### ➕ Get started")
        with st.form(key="CreateForm", border=True):
            selected_release_entity = st.selectbox(
                label="Release Type",
                options=RELEASE_TYPE_TABLE.get_all_beans(),
                format_func=lambda enetity: enetity.label_en,
                key="ReleaseTypeSelectBox",
            )
            inputed_title = st.text_input(
                label="Title",
                placeholder="Enter room title here.",
                key="RoomTitleTextInput",
            )
            message_area = st.empty()
            _, button_area, _ = st.columns([5, 3, 5])
            with button_area:
                is_pushed = st.form_submit_button(label="Create", type="primary", use_container_width=True)
            _, loading_area, _ = st.columns([1, 1, 1])

        return CreateActionResults(
            title=inputed_title,
            release_entity=selected_release_entity,
            message_area=message_area,
            loading_area=loading_area,
            is_pushed=is_pushed,
        )

    @staticmethod
    def _display_room_container_and_get_results(chat_room_dto: ChatRoomDto, chat_room_type: Literal["Edit", "View"], container_id: int) -> RoomContainerActionResults:
        with st.container(border=True):
            contents = dedent(
                f"""
                ##### 📝 {chat_room_dto.room_title}  
                👤 {chat_room_dto.account_family_name_en} {chat_room_dto.account_given_name_en}  
                🕛 {chat_room_dto.room_created_at_short}  
                👀 {chat_room_dto.release_label_en}
                """
            )
            st.markdown(contents)

            _, loading_area, _ = st.columns([1, 2, 1])
            _, button_area, _ = st.columns([1, 2, 1])
            is_pushed = button_area.button(label=chat_room_type, type="primary", key=f"Room{chat_room_type}Button{container_id}", use_container_width=True)

        return RoomContainerActionResults(
            is_pushed=is_pushed,
            loading_area=loading_area,
        )

    @classmethod
    def _display_room_containers_and_get_results(cls) -> Optional[EnterActionResults]:
        main_home_manager = SStates.LoadedMainHomeManager.get()
        selected_chat_room_dto = None
        selected_loading_area = None
        left_area, right_area = st.columns([1, 1])

        with left_area:
            st.markdown("#### 🧍 Yours")
            for container_id, chat_room_dto in enumerate(main_home_manager.get_yours_chat_room_dtos()):
                action_results = cls._display_room_container_and_get_results(
                    chat_room_dto=chat_room_dto,
                    chat_room_type="Edit",
                    container_id=container_id,
                )
                if action_results.is_pushed:
                    selected_chat_room_dto = chat_room_dto
                    selected_loading_area = action_results.loading_area
        
        with right_area:
            st.markdown("#### 🧑‍🤝‍🧑 Everyone")
            for container_id, chat_room_dto in enumerate(main_home_manager.get_everyone_chat_room_dtos()):
                action_results = cls._display_room_container_and_get_results(
                    chat_room_dto=chat_room_dto,
                    chat_room_type="View",
                    container_id=container_id,
                )
                if action_results.is_pushed:
                    selected_chat_room_dto = chat_room_dto
                    selected_loading_area = action_results.loading_area

        if selected_chat_room_dto == None:
            return None
        if selected_loading_area == None:
            return None

        return EnterActionResults(
            chat_room_dto=selected_chat_room_dto,
            loading_area=selected_loading_area,
        )

    @staticmethod
    def _execute_create_process(create_action_results: CreateActionResults) -> bool:
        if not create_action_results.is_pushed:
            return False

        with create_action_results.loading_area:
            with st_lottie_spinner(animation_source=LoadedLottie.LOADING):
                processer_manager = SStates.CreateChatRoomProcess.get()
                response = processer_manager.run_all(
                    message_area=create_action_results.message_area,
                    title=create_action_results.title,
                    release_entity=create_action_results.release_entity,
                )

        if not response.is_success:
            create_action_results.message_area.warning(response.message)
            return False

        create_action_results.message_area.empty()
        ChatRoomPreComponent.prepare()
        return True

    @staticmethod
    def _execute_enter_process(enter_action_results: Optional[EnterActionResults]) -> bool:
        if not enter_action_results:
            return False

        with enter_action_results.loading_area:
            with st_lottie_spinner(animation_source=LoadedLottie.LOADING):
                processer_manager = SStates.EnterChatRoomProcess.get()
                response = processer_manager.run_all(
                    room_id=enter_action_results.chat_room_dto.room_id,
                )
        if not response.is_success:
            return False

        ChatRoomPreComponent.prepare()
        return True

    @classmethod
    def _on_click_accounts(cls) -> None:
        AccountPreComponent.prepare()
        cls.deinit()

    @classmethod
    def _on_click_sign_out(cls) -> None:
        SignInPreComponent.prepare()
        cls.deinit()

    @classmethod
    def main(cls) -> None:
        cls._display_titles()
        cls._display_sidebar_titles()
        cls._display_overview()

        create_action_results = cls._display_create_form_and_get_results()
        enter_action_results = cls._display_room_containers_and_get_results()

        is_success = cls._execute_create_process(create_action_results=create_action_results)
        if is_success:
            cls.deinit()
            st.rerun()

        is_success = cls._execute_enter_process(enter_action_results=enter_action_results)
        if is_success:
            cls.deinit()
            st.rerun()

    @staticmethod
    def deinit() -> None:
        SStates.CreateChatRoomProcess.deinit()
        SStates.EnterChatRoomProcess.deinit()
        SStates.LoadedMainHomeManager.deinit()
        SignInPreComponent.deinit()
        ChatRoomPreComponent.deinit()
        AccountPreComponent.deinit()
