import streamlit as st
from streamlit_lottie import st_lottie_spinner
from streamlit.delta_generator import DeltaGenerator

from ...base import BaseComponent
from .. import s_states as SStates
from .home_pre_component import HomePreComponent
from .chat_room_action_results import QueryActionResults, ReturnHomeActionResults
from model import ASSISTANT_TYPE_TABLE, LoadedLottie, LoadedImage


class ChatRoomComponent(BaseComponent):
    @staticmethod
    def init() -> None:
        SStates.CurrentComponentEntity.init()
        SStates.SignedInAccountEntity.validate()
        SStates.EnteredChatRoomManager.init()
        SStates.QueryProcess.init()
        HomePreComponent.init()

    @staticmethod
    def _display_titles() -> None:
        current_component_entity = SStates.CurrentComponentEntity.get()
        st.markdown(f"### {current_component_entity.label_en}")

    @classmethod
    def _display_sidebar_titles_and_get_results(cls) -> ReturnHomeActionResults:
        st.sidebar.image(image=LoadedImage.LOGO, use_column_width=True)
        is_pushed = st.sidebar.button(label="🏠 Home", key="ReturnHomeButton", use_container_width=True)
        _, loading_area, _ = st.sidebar.columns([1, 2, 1])
        return ReturnHomeActionResults(loading_area=loading_area, is_pushed=is_pushed)

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

            _, left_area, _, center_area, _, right_area, _ = st.columns([1, 3, 1, 3, 1, 3, 1])
            with left_area:
                is_run_pushed = st.form_submit_button(label="Run", type="primary", use_container_width=True)
            with center_area:
                is_rerun_pushed = st.form_submit_button(label="Rerun", type="primary", use_container_width=True)
            with right_area:
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
            action_results = cls._display_query_form_and_get_results()
            history_area = cls._display_history()

            is_success = cls._execute_return_home_process(action_results=return_home_action_results)
            if is_success:
                cls.deinit()
                st.rerun()
            cls._execute_query_process(action_results=action_results, history_area=history_area)

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
        HomePreComponent.deinit()
