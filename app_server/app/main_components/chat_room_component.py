import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from .chat_room_action_results import ActionResults
from ..base import BaseComponent
from ..main_s_states import AccountSState, MainComponentSState, QueryProcesserSState, ChatRoomSState
from model import ASSISTANT_TYPE_TABLE


class ChatRoomComponent(BaseComponent):
    @staticmethod
    def init() -> None:
        AccountSState.init()
        ChatRoomSState.init()
        QueryProcesserSState.init()

    @classmethod
    def _display_sign_out_button(cls) -> None:
        st.sidebar.button(label="👤 Sign out", key="SignOutButton", on_click=cls._on_click_sign_out, use_container_width=True)

    @classmethod
    def _display_return_home_button(cls) -> None:
        st.sidebar.button(label="🏠 Home", key="ReturnHomeButton", on_click=cls._on_click_return_home, use_container_width=True)

    @staticmethod
    def _display_title() -> None:
        current_component_entity = MainComponentSState.get()
        st.markdown(f"### {current_component_entity.label_en}")

    @staticmethod
    def _display_query_form_and_get_results() -> ActionResults:
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

        return ActionResults(
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
            chat_room_manager = ChatRoomSState.get()
            for message_entity in chat_room_manager.get_all_message_entities():
                if message_entity.role_id == "system":
                    continue
                with st.chat_message(name=message_entity.role_id):
                    st.write(message_entity.content)
        return history_area

    @staticmethod
    def _execute_query_process(action_results: ActionResults, history_area: DeltaGenerator) -> None:
        processer_manager = QueryProcesserSState.get()
        if action_results.is_rerun_pushed or action_results.is_cancel_pushed:
            processer_manager.init_processers()

        if action_results.is_run_pushed or action_results.is_rerun_pushed:
            processer_manager.run_all(
                message_area=action_results.message_area,
                history_area=history_area,
                assistant_entity=action_results.assistant_entity,
                prompt=action_results.prompt,
            )

    @classmethod
    def _on_click_sign_out(cls):
        MainComponentSState.set_sign_in_entity()
        cls.deinit()
        AccountSState.deinit()

    @classmethod
    def _on_click_return_home(cls):
        MainComponentSState.set_home_entity()
        cls.deinit()

    @classmethod
    def main(cls) -> None:
        cls._display_sign_out_button()
        cls._display_return_home_button()
        cls._display_title()

        is_created_user = ChatRoomSState.get().account_id == AccountSState.get().account_id
        if is_created_user:
            action_results = cls._display_query_form_and_get_results()
            history_area = cls._display_history()
            cls._execute_query_process(action_results=action_results, history_area=history_area)
        else:
            history_area = cls._display_history()
            return

    @staticmethod
    def deinit() -> None:
        ChatRoomSState.deinit()
        QueryProcesserSState.deinit()
