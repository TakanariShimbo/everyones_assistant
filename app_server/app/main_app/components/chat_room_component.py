from typing import Optional

import streamlit as st
from streamlit_lottie import st_lottie_spinner
from streamlit.delta_generator import DeltaGenerator

from ...base import BaseComponent
from ...handler import TextHandler
from .. import s_states as SStates
from .home_pre_component import HomePreComponent
from .chat_room_action_results import QueryActionResults, ReturnHomeActionResults, MenusActionResults, EnterActionResults
from model import ASSISTANT_TYPE_TABLE, LoadedLottie, LoadedImage


class ChatRoomComponent(BaseComponent):
    @staticmethod
    def init() -> None:
        SStates.CurrentComponentEntity.init()
        SStates.SignedInAccountEntity.validate()
        SStates.EnteredChatRoomManager.validate()
        SStates.QueryProcess.init()
        SStates.DeleteChatRoomProcess.init()
        HomePreComponent.init()

    @staticmethod
    def _display_titles() -> None:
        chat_room_manager = SStates.EnteredChatRoomManager.get()
        st.markdown(f"### 💬 {TextHandler.truncate(text=chat_room_manager.title, max_length=22)}")

    @classmethod
    def _display_sidebar_titles_and_get_results(cls) -> ReturnHomeActionResults:
        st.sidebar.image(image=LoadedImage.LOGO, use_column_width=True)
        is_pushed = st.sidebar.button(label="🏠 Home", key="ReturnHomeButton", use_container_width=True)
        _, loading_area, _ = st.sidebar.columns([1, 2, 1])
        return ReturnHomeActionResults(loading_area=loading_area, is_pushed=is_pushed)

    @classmethod
    def _display_sidebar_menus_and_get_results(cls) -> MenusActionResults:
        st.sidebar.markdown("## Menus")
        is_pushed = st.sidebar.button(label="🗑️ Delete", key="DeleteChatRoomButton", use_container_width=True)
        _, loading_area, _ = st.sidebar.columns([1, 2, 1])
        return MenusActionResults(loading_area=loading_area, is_pushed=is_pushed)

    @classmethod
    def _display_room_buttons_and_get_results(cls) -> Optional[EnterActionResults]:
        st.sidebar.markdown("## Rooms")
        selected_chat_room_entity = None
        chat_room_manager = SStates.EnteredChatRoomManager.get()
        for button_id, chat_room_entity in enumerate(chat_room_manager.get_all_chat_room_entities()):
            is_pushed = st.sidebar.button(
                label=TextHandler.truncate(text=chat_room_entity.title, max_length=22), 
                key=f"RoomButton{button_id}", 
                use_container_width=True,
            )
            if is_pushed:
                selected_chat_room_entity = chat_room_entity
        _, loading_area, _ = st.sidebar.columns([1, 2, 1])
        if selected_chat_room_entity == None:
            return None
        return EnterActionResults(chat_room_entity=selected_chat_room_entity, loading_area=loading_area)

    @staticmethod
    def _display_query_form_and_get_results() -> QueryActionResults:
        st.markdown("#### ❔ Query")
        form_area = st.form(key="QueryForm")
        with form_area:
            selected_assistant_entity = st.selectbox(
                label="Assistant Type",
                options=ASSISTANT_TYPE_TABLE.get_all_beans(),
                format_func=lambda enetity: enetity.label_en,
                key="AssistantTypeSelectBox",
            )

            inputed_prompt = st.text_area(
                label="Prompt",
                placeholder="Enter prompt here.",
                key="PromptTextArea",
            )

            message_area = st.empty()

            _, run_button_area, _, rerun_button_area, _, cancel_button_area, _ = st.columns([1, 3, 1, 3, 1, 3, 1])
            with run_button_area:
                is_run_pushed = st.form_submit_button(label="Run", type="primary", use_container_width=True)
            with rerun_button_area:
                is_rerun_pushed = st.form_submit_button(label="Rerun", type="primary", use_container_width=True)
            with cancel_button_area:
                is_cancel_pushed = st.form_submit_button(label="Cancel", type="secondary", use_container_width=True)

        return QueryActionResults(
            assistant_entity=selected_assistant_entity,
            prompt=inputed_prompt,
            message_area=message_area,
            is_run_pushed=is_run_pushed,
            is_rerun_pushed=is_rerun_pushed,
            is_cancel_pushed=is_cancel_pushed,
        )

    @staticmethod
    def _display_history() -> DeltaGenerator:
        history_area = st.container(border=False)
        with history_area:
            st.markdown("#### 📝 History")
            chat_room_manager = SStates.EnteredChatRoomManager.get()
            for message_entity in chat_room_manager.get_all_message_entities():
                if message_entity.role_id == "system":
                    continue
                with st.chat_message(name=message_entity.role_id):
                    st.write(message_entity.content)
        return history_area

    @staticmethod
    def _execute_return_home_process(action_results: ReturnHomeActionResults) -> bool:
        if not action_results.is_pushed:
            return False

        with action_results.loading_area:
            with st_lottie_spinner(animation_source=LoadedLottie.LOADING):
                HomePreComponent.prepare()
        return True

    @staticmethod
    def _execute_menus_process(action_results: MenusActionResults) -> bool:
        if not action_results.is_pushed:
            return False

        with action_results.loading_area:
            with st_lottie_spinner(animation_source=LoadedLottie.LOADING):
                processer_manager = SStates.DeleteChatRoomProcess.get()
                processer_manager.run_all()
                HomePreComponent.prepare()
        return True

    @staticmethod
    def _execute_enter_process(enter_action_results: Optional[EnterActionResults]) -> bool:
        if not enter_action_results:
            return False

        with enter_action_results.loading_area:
            with st_lottie_spinner(animation_source=LoadedLottie.LOADING):
                processer_manager = SStates.EnterChatRoomProcess.get()
                response = processer_manager.run_all(
                    room_id=enter_action_results.chat_room_entity.room_id,
                )
        if not response.is_success:
            return False
        return True

    @staticmethod
    def _execute_query_process(action_results: QueryActionResults, history_area: DeltaGenerator) -> None:
        processer_manager = SStates.QueryProcess.get()
        if action_results.is_rerun_pushed or action_results.is_cancel_pushed:
            processer_manager.init_processers()

        if action_results.is_run_pushed or action_results.is_rerun_pushed:
            response = processer_manager.run_all(
                message_area=action_results.message_area,
                history_area=history_area,
                assistant_entity=action_results.assistant_entity,
                prompt=action_results.prompt,
            )
            if not response.is_success:
                action_results.message_area.warning(response.message)
            action_results.message_area.empty()

    @classmethod
    def main(cls) -> None:
        cls._display_titles()
        is_created_user = SStates.EnteredChatRoomManager.get().account_id == SStates.SignedInAccountEntity.get().account_id
        if is_created_user:
            return_home_action_results = cls._display_sidebar_titles_and_get_results()
            menus_action_results = cls._display_sidebar_menus_and_get_results()
            enter_action_results = cls._display_room_buttons_and_get_results()
            query_action_results = cls._display_query_form_and_get_results()
            history_area = cls._display_history()

            is_success = cls._execute_return_home_process(action_results=return_home_action_results)
            if is_success:
                cls.deinit()
                st.rerun()
            is_success = cls._execute_menus_process(action_results=menus_action_results)
            if is_success:
                cls.deinit()
                st.rerun()
            is_success = cls._execute_enter_process(enter_action_results=enter_action_results)
            if is_success:
                st.rerun()
            cls._execute_query_process(action_results=query_action_results, history_area=history_area)

        else:
            return_home_action_results = cls._display_sidebar_titles_and_get_results()
            history_area = cls._display_history()

            is_success = cls._execute_return_home_process(action_results=return_home_action_results)
            if is_success:
                cls.deinit()
                st.rerun()

    @staticmethod
    def deinit() -> None:
        SStates.EnteredChatRoomManager.deinit()
        SStates.QueryProcess.deinit()
        SStates.DeleteChatRoomProcess.deinit()
        HomePreComponent.deinit()
