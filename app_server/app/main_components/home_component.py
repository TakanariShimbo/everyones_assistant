from textwrap import dedent
from typing import Optional, Literal

import streamlit as st
from streamlit_lottie import st_lottie_spinner

from .home_action_results import CreateActionResults, EnterActionResults, RoomContainerActionResults
from ..base import BaseComponent
from ..main_s_states import AccountSState, MainComponentSState, CreateProcesserSState, EnterProcesserSState
from model import ChatRoomDtoTable, ChatRoomDto, RELEASE_TYPE_TABLE, LoadedLottie, Database


class HomeComponent(BaseComponent):
    @staticmethod
    def init() -> None:
        AccountSState.init()
        CreateProcesserSState.init()
        EnterProcesserSState.init()

    @classmethod
    def _display_sign_out_button(cls) -> None:
        st.sidebar.button(label="👤 Sign out", key="SignOutButton", on_click=cls._on_click_sign_out, use_container_width=True)

    @staticmethod
    def _display_title() -> None:
        current_component_entity = MainComponentSState.get()
        st.markdown(f"### {current_component_entity.label_en}")

    @staticmethod
    def _display_overview() -> None:
        content = dedent(
            f"""
            #### 🔎 Overview
            Welcome to Everyone's Assistant.   
            Experience the forefront of AI technology and explore the possibilities of the future.  
            AI makes your daily life smarter and easier.  
            """
        )
        st.markdown(content)

    @staticmethod
    def _display_create_form_and_get_results() -> CreateActionResults:
        st.markdown("#### ➕ New")
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
    def _display_rooms_and_get_results(cls) -> Optional[EnterActionResults]:
        selected_chat_room_dto = None
        selected_loading_area = None
        left_area, right_area = st.columns([1, 1])

        with left_area:
            st.markdown("#### 🧍 Yours")
            with st_lottie_spinner(animation_source=LoadedLottie.LOADING):
                your_room_table = ChatRoomDtoTable.load_specified_account_from_database(
                    database_engine=Database.ENGINE,
                    account_id=AccountSState.get().account_id,
                )
            for container_id, chat_room_dto in enumerate(your_room_table.get_all_beans()):
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
            with st_lottie_spinner(animation_source=LoadedLottie.LOADING):
                your_room_table = ChatRoomDtoTable.load_public_unspecified_account_from_database(
                    database_engine=Database.ENGINE,
                    account_id=AccountSState.get().account_id,
                )
            for container_id, chat_room_dto in enumerate(your_room_table.get_all_beans()):
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
                processers_manager = CreateProcesserSState.get()
                is_success = processers_manager.run_all(
                    message_area=create_action_results.message_area,
                    title=create_action_results.title,
                    release_entity=create_action_results.release_entity,
                )
        return is_success

    @staticmethod
    def _execute_enter_process(enter_action_results: Optional[EnterActionResults]) -> bool:
        if not enter_action_results:
            return False

        with enter_action_results.loading_area:
            with st_lottie_spinner(animation_source=LoadedLottie.LOADING):
                processers_manager = EnterProcesserSState.get()
                is_success = processers_manager.run_all(
                    room_id=enter_action_results.chat_room_dto.room_id,
                    account_id=enter_action_results.chat_room_dto.account_id,
                    release_id=enter_action_results.chat_room_dto.release_id,
                )
        return is_success

    @classmethod
    def _on_click_sign_out(cls) -> None:
        MainComponentSState.set_sign_in_entity()
        cls.deinit()
        AccountSState.deinit()

    @classmethod
    def main(cls) -> None:
        cls._display_sign_out_button()
        cls._display_title()
        cls._display_overview()

        create_action_results = cls._display_create_form_and_get_results()
        enter_action_results = cls._display_rooms_and_get_results()

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
        CreateProcesserSState.deinit()
        EnterProcesserSState.deinit()
