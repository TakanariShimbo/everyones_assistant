import streamlit as st

from .sign_in_action_results import ActionResults
from ..base import BaseComponent
from ..management_s_states import ManagementComponentSState
from model import LoadedEnv


class SignInComponent(BaseComponent):
    @staticmethod
    def init() -> None:
        pass

    @staticmethod
    def _display_title() -> None:
        current_component_entity = ManagementComponentSState.get()
        st.markdown(f"### {current_component_entity.label_en}")

    @staticmethod
    def _display_sign_in_form_and_get_results() -> ActionResults:
        with st.form(key="SignInForm", border=True):
            inputed_admin_id = st.text_input(
                label="Admin ID",
                placeholder="Enter admin id here.",
                key="AdminIdTextInput",
            )
            inputed_admin_password = st.text_input(
                label="Password",
                placeholder="Enter password here.",
                key="PasswordTextInput",
                type="password",
            )
            message_area = st.empty()
            _, button_area, _ = st.columns([5, 3, 5])
            with button_area:
                is_pushed = st.form_submit_button(label="Enter", type="primary", use_container_width=True)

        return ActionResults(
            admin_id=inputed_admin_id,
            admin_password=inputed_admin_password,
            message_area=message_area,
            is_pushed=is_pushed,
        )

    @staticmethod
    def _execute_sign_in_process(action_results: ActionResults) -> bool:
        if not action_results.is_pushed:
            return False

        if not action_results.admin_id == LoadedEnv.admin_id:
            action_results.message_area.warning("Please input form corectly.")
            return False
        
        if not action_results.admin_password == LoadedEnv.admin_password:
            action_results.message_area.warning("Please input form corectly.")
            return False
        
        ManagementComponentSState.set_home_entity()
        return True

    @classmethod
    def main(cls) -> None:
        cls._display_title()
        action_results = cls._display_sign_in_form_and_get_results()
        is_success = cls._execute_sign_in_process(action_results=action_results)
        if is_success:
            cls.deinit()
            st.rerun()

    @staticmethod
    def deinit() -> None:
        pass
