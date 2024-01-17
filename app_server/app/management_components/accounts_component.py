import streamlit as st
from streamlit_lottie import st_lottie_spinner

from .accounts_action_results import ActionResults
from ..base import BaseComponent
from ..management_s_states import ManagementComponentSState, SignUpProcesserSState
from model import AccountTable, Database, LoadedLottie


class AccountsComponent(BaseComponent):
    @staticmethod
    def init() -> None:
        SignUpProcesserSState.init()

    @classmethod
    def _display_sign_out_button(cls) -> None:
        st.sidebar.button(label="👤 Sign out", key="SignOutButton", on_click=cls._on_click_sign_out, use_container_width=True)

    @classmethod
    def _display_return_home_button(cls) -> None:
        st.sidebar.button(label="🏠 Home", key="ReturnHomeButton", on_click=cls._on_click_return_home, use_container_width=True)

    @staticmethod
    def _display_title() -> None:
        current_component_entity = ManagementComponentSState.get()
        st.markdown(f"### {current_component_entity.label_en}")

    @staticmethod
    def _display_sign_up_form_and_get_results() -> ActionResults:
        with st.form(key="SignUpForm", border=True):
            left_area, right_area = st.columns([1,1])
            with left_area:
                inputed_account_id = st.text_input(
                    label="Account ID",
                    placeholder="Enter account id here.",
                    key="AccountIdTextInput",
                )
            with right_area:
                inputed_mail_address = st.text_input(
                    label="Email Address",
                    placeholder="Enter your email here.",
                    key="MailAddressTextInput",
                )

            left_area, right_area = st.columns([1,1])
            with left_area:
                inputed_family_name_en = st.text_input(
                    label="Family Name (English)",
                    placeholder="Enter your family name in English here.",
                    key="FamilyNameEnTextInput",
                )
            with right_area:
                inputed_given_name_en = st.text_input(
                    label="Given Name (English)",
                    placeholder="Enter your given name in English here.",
                    key="GivenNameEnTextInput",
                )

            left_area, right_area = st.columns([1,1])
            with left_area:
                inputed_family_name_jp = st.text_input(
                    label="Family Name (Japanese)",
                    placeholder="Enter your family name in Japanese here.",
                    key="FamilyNameJpTextInput",
                )
            with right_area:
                inputed_given_name_jp = st.text_input(
                    label="Given Name (Japanese)",
                    placeholder="Enter your given name in Japanese here.",
                    key="GivenNameJpTextInput",
                )

            left_area, right_area = st.columns([1,1])
            with left_area:
                inputed_raw_password = st.text_input(
                    label="Password",
                    placeholder="Enter password here.",
                    key="PasswordTextInput",
                    type="password",
                )
            with right_area:
                inputed_raw_password_confirm = st.text_input(
                    label="Password (Confirm)",
                    placeholder="Enter password again for confirmation here.",
                    key="ConfirmPasswordTextInput",
                    type="password",
                )

            message_area = st.empty()
            _, button_area, _ = st.columns([5, 3, 5])
            with button_area:
                is_pushed = st.form_submit_button(label="Register", type="primary", use_container_width=True)
            _, loading_area, _ = st.columns([1, 1, 1])

        return ActionResults(
            account_id=inputed_account_id,
            mail_address=inputed_mail_address,
            family_name_en=inputed_family_name_en,
            given_name_en=inputed_given_name_en,
            family_name_jp=inputed_family_name_jp,
            given_name_jp=inputed_given_name_jp,
            raw_password=inputed_raw_password,
            raw_password_confirm=inputed_raw_password_confirm,
            message_area=message_area,
            loading_area=loading_area,
            is_pushed=is_pushed,
        )

    @staticmethod
    def _execute_sign_up_process(action_results: ActionResults) -> None:
        if not action_results.is_pushed:
            return

        with action_results.loading_area:
            with st_lottie_spinner(animation_source=LoadedLottie.LOADING):
                processers_manager = SignUpProcesserSState.get()
                processers_manager.run_all(
                    message_area=action_results.message_area,
                    account_id=action_results.account_id,
                    mail_address=action_results.mail_address,
                    family_name_en=action_results.family_name_en,
                    given_name_en=action_results.given_name_en,
                    family_name_jp=action_results.family_name_jp,
                    given_name_jp=action_results.given_name_jp,
                    raw_password=action_results.raw_password,
                    raw_password_confirm=action_results.raw_password_confirm,
                )

    @staticmethod
    def _display_account_table() -> None:
        account_table = AccountTable.load_from_database(database_engine=Database.ENGINE)
        st.dataframe(account_table.df, use_container_width=True)

    @classmethod
    def _on_click_sign_out(cls):
        ManagementComponentSState.set_sign_in_entity()
        cls.deinit()

    @classmethod
    def _on_click_return_home(cls):
        ManagementComponentSState.set_home_entity()
        cls.deinit()

    @classmethod
    def main(cls) -> None:
        cls._display_sign_out_button()
        cls._display_return_home_button()
        cls._display_title()
        action_results = cls._display_sign_up_form_and_get_results()
        cls._execute_sign_up_process(action_results=action_results)
        cls._display_account_table()

    @staticmethod
    def deinit() -> None:
        SignUpProcesserSState.deinit()