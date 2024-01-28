import streamlit as st
from streamlit_lottie import st_lottie_spinner

from ...base import BaseComponent
from .. import s_states as SStates
from .. import q_params as QParams
from ..pre_components.home import HomePreComponent
from ..action_results.sign_in import ActionResults
from model import LoadedLottie


class SignInComponent(BaseComponent):
    @staticmethod
    def init() -> None:
        SStates.CurrentComponentEntity.init()
        QParams.ComponentId.set(value=SStates.CurrentComponentEntity.get().component_id)
        SStates.SignInProcess.init()
        HomePreComponent.init()

    @staticmethod
    def _display_title() -> None:
        current_component_entity = SStates.CurrentComponentEntity.get()
        st.markdown(f"### {current_component_entity.label_en}")

    @staticmethod
    def _display_sign_in_form_and_get_results() -> ActionResults:
        with st.form(key="SignInForm", border=True):
            inputed_account_id = st.text_input(
                label="Account ID",
                placeholder="Enter account id here.",
                key="AccountIdTextInput",
            )
            inputed_raw_password = st.text_input(
                label="Password",
                placeholder="Enter password here.",
                key="PasswordTextInput",
                type="password",
            )
            message_area = st.empty()
            _, button_area, _ = st.columns([5, 3, 5])
            with button_area:
                is_pushed = st.form_submit_button(label="Enter", type="primary", use_container_width=True)
            _, loading_area, _ = st.columns([1, 1, 1])

        return ActionResults(
            account_id=inputed_account_id,
            raw_password=inputed_raw_password,
            message_area=message_area,
            loading_area=loading_area,
            is_pushed=is_pushed,
        )

    @staticmethod
    def _execute_sign_in_process(action_results: ActionResults) -> bool:
        if not action_results.is_pushed:
            return False

        with action_results.loading_area:
            with st_lottie_spinner(animation_source=LoadedLottie.LOADING):
                processer_manager = SStates.SignInProcess.get()
                response = processer_manager.run_all(
                    message_area=action_results.message_area,
                    account_id=action_results.account_id,
                    raw_password=action_results.raw_password,
                )

                if not response.is_success:
                    action_results.message_area.warning(response.message)
                    return False

                action_results.message_area.empty()
                HomePreComponent.prepare()
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
        SStates.SignInProcess.deinit()
        HomePreComponent.deinit()
