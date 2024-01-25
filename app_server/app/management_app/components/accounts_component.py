import streamlit as st
from streamlit_lottie import st_lottie_spinner

from ...base import BaseComponent
from .. import s_states as SStates
from .home_pre_component import HomePreComponent
from .accounts_action_results import SignUpActionResults, AccountTableIOActionResults
from model import LoadedLottie, LoadedImage


class AccountsComponent(BaseComponent):
    @staticmethod
    def init() -> None:
        SStates.CurrentComponentEntity.init()
        SStates.SignUpProcess.init()
        SStates.AccountsDataEditorKey.init()
        SStates.LoadedAccountTable.validate()
        HomePreComponent.init()

    @staticmethod
    def _display_titles() -> None:
        current_component_entity = SStates.CurrentComponentEntity.get()
        st.markdown(f"### {current_component_entity.label_en}")

    @classmethod
    def _display_sidebar_titles(cls) -> None:
        st.sidebar.image(image=LoadedImage.LOGO, use_column_width=True)
        st.sidebar.button(label="🏠 Home", key="ReturnHomeButton", on_click=cls._on_click_return_home, use_container_width=True)

    @staticmethod
    def _display_sign_up_form_and_get_results() -> SignUpActionResults:
        st.markdown("#### ➕ Sign up")
        with st.form(key="SignUpForm", border=True):
            left_area, right_area = st.columns([1, 1])
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

            left_area, right_area = st.columns([1, 1])
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

            left_area, right_area = st.columns([1, 1])
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

            left_area, right_area = st.columns([1, 1])
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
                    key="PasswordConfirmTextInput",
                    type="password",
                )

            message_area = st.empty()
            _, button_area, _ = st.columns([5, 3, 5])
            with button_area:
                is_pushed = st.form_submit_button(label="Register", type="primary", use_container_width=True)
            _, loading_area, _ = st.columns([1, 1, 1])

        return SignUpActionResults(
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
    def _display_account_table_and_get_results() -> AccountTableIOActionResults:
        st.markdown("#### ✍️ Edit Accounts")
        with st.container(border=True):
            account_table = SStates.LoadedAccountTable.get()
            st.data_editor(
                data=account_table.display_df,
                disabled=account_table.uneditable_columns,
                hide_index=True, 
                use_container_width=True,
                key=f"AccountTableDataEditor{SStates.AccountsDataEditorKey.get()}",
            )

            _, button_area, _ = st.columns([5, 3, 5])
            with button_area:
                is_pushed = st.button(label="Load", type="primary", key="LoadAccountTableButton", use_container_width=True)
            _, loading_area, _ = st.columns([1, 1, 1])

        return AccountTableIOActionResults(
            loading_area=loading_area,
            is_pushed=is_pushed,
        )

    @staticmethod
    def _execute_sign_up_process(action_results: SignUpActionResults) -> bool:
        if not action_results.is_pushed:
            return False

        with action_results.loading_area:
            with st_lottie_spinner(animation_source=LoadedLottie.LOADING):
                processer_manager = SStates.SignUpProcess.get()
                response = processer_manager.run_all(
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

        if not response.is_success:
            action_results.message_area.warning(response.message)
            return False

        action_results.message_area.success(response.message)
        return True

    @staticmethod
    def _execute_account_table_io_process(action_results: AccountTableIOActionResults) -> bool:
        if not action_results.is_pushed:
            return False

        with action_results.loading_area:
            with st_lottie_spinner(animation_source=LoadedLottie.LOADING):
                processer_manager = SStates.LoadAccountTableProcess.get()
                processer_manager.run_all()
                SStates.AccountsDataEditorKey.change_key()
        return True

    @classmethod
    def _on_click_return_home(cls):
        HomePreComponent.prepare()
        cls.deinit()

    @classmethod
    def main(cls) -> None:
        cls._display_titles()
        cls._display_sidebar_titles()
        sign_up_action_results = cls._display_sign_up_form_and_get_results()
        account_table_io_action_results = cls._display_account_table_and_get_results()
        
        cls._execute_sign_up_process(action_results=sign_up_action_results)
        is_success = cls._execute_account_table_io_process(action_results=account_table_io_action_results)
        if is_success:
            cls.deinit()
            st.rerun()

    @staticmethod
    def deinit() -> None:
        SStates.SignUpProcess.deinit()
        SStates.LoadedAccountTable.deinit()
        SStates.AccountsDataEditorKey.deinit()
        HomePreComponent.deinit()
