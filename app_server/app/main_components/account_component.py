import streamlit as st
from streamlit_lottie import st_lottie_spinner

from .account_action_results import EditInfoActionResults, ChangePassActionResults
from ..base import BaseComponent
from ..main_s_states import MainComponentSState, AccountSState, EditAccountInfoProcesserSState, ChangeAccountPassProcesserSState
from model import LoadedLottie


class AccountComponent(BaseComponent):
    @staticmethod
    def init() -> None:
        AccountSState.init()
        EditAccountInfoProcesserSState.init()
        ChangeAccountPassProcesserSState.init()

    @staticmethod
    def _display_titles() -> None:
        current_component_entity = MainComponentSState.get()
        st.markdown(f"### {current_component_entity.label_en}")
        st.sidebar.markdown("## Menes")

    @classmethod
    def _display_return_home_button(cls) -> None:
        st.sidebar.button(label="🏠 Home", key="ReturnHomeButton", on_click=cls._on_click_return_home, use_container_width=True)

    @staticmethod
    def _display_edit_info_form_and_get_results() -> EditInfoActionResults:
        self_account_entity = AccountSState.get()

        st.markdown("#### 📝 Information")
        with st.form(key="EditInfoForm", border=True):
            left_area, right_area = st.columns([1, 1])
            with left_area:
                st.text_input(
                    label="Account ID",
                    placeholder="Enter account id here.",
                    key="AccountIdTextInput",
                    value=self_account_entity.account_id,
                    disabled=True,
                )
            with right_area:
                inputed_mail_address = st.text_input(
                    label="Email Address",
                    placeholder="Enter your email here.",
                    key="MailAddressTextInput",
                    value=self_account_entity.mail_address,
                )

            left_area, right_area = st.columns([1, 1])
            with left_area:
                inputed_family_name_en = st.text_input(
                    label="Family Name (English)",
                    placeholder="Enter your family name in English here.",
                    key="FamilyNameEnTextInput",
                    value=self_account_entity.family_name_en,
                )
            with right_area:
                inputed_given_name_en = st.text_input(
                    label="Given Name (English)",
                    placeholder="Enter your given name in English here.",
                    key="GivenNameEnTextInput",
                    value=self_account_entity.given_name_en,
                )

            left_area, right_area = st.columns([1, 1])
            with left_area:
                inputed_family_name_jp = st.text_input(
                    label="Family Name (Japanese)",
                    placeholder="Enter your family name in Japanese here.",
                    key="FamilyNameJpTextInput",
                    value=self_account_entity.family_name_jp,
                )
            with right_area:
                inputed_given_name_jp = st.text_input(
                    label="Given Name (Japanese)",
                    placeholder="Enter your given name in Japanese here.",
                    key="GivenNameJpTextInput",
                    value=self_account_entity.given_name_jp,
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
                is_pushed = st.form_submit_button(label="Update", type="primary", use_container_width=True)
            _, loading_area, _ = st.columns([1, 1, 1])

        return EditInfoActionResults(
            account_id=self_account_entity.account_id,
            mail_address=inputed_mail_address,
            family_name_en=inputed_family_name_en,
            given_name_en=inputed_given_name_en,
            family_name_jp=inputed_family_name_jp,
            given_name_jp=inputed_given_name_jp,
            raw_password=inputed_raw_password,
            message_area=message_area,
            loading_area=loading_area,
            is_pushed=is_pushed,
        )

    @staticmethod
    def _display_change_pass_form_and_get_results() -> ChangePassActionResults:
        self_account_entity = AccountSState.get()

        st.markdown("#### 🔑 Password")
        with st.form(key="ChangePassForm", border=True):
            inputed_current_raw_password = st.text_input(
                label="Current Password",
                placeholder="Enter current password here.",
                key="CurrentPasswordTextInput",
                type="password",
            )

            left_area, right_area = st.columns([1, 1])
            with left_area:
                inputed_new_raw_password = st.text_input(
                    label="New Password",
                    placeholder="Enter new password here.",
                    key="NewPasswordTextInput",
                    type="password",
                )
            with right_area:
                inputed_new_raw_password_confirm = st.text_input(
                    label="New Password (Confirm)",
                    placeholder="Enter password again for confirmation here.",
                    key="NewPasswordConfirmTextInput",
                    type="password",
                )             

            message_area = st.empty()
            _, button_area, _ = st.columns([5, 3, 5])
            with button_area:
                is_pushed = st.form_submit_button(label="Change", type="primary", use_container_width=True)
            _, loading_area, _ = st.columns([1, 1, 1])

        return ChangePassActionResults(
            account_id=self_account_entity.account_id,
            current_raw_password=inputed_current_raw_password,
            new_raw_password=inputed_new_raw_password,
            new_raw_password_confirm=inputed_new_raw_password_confirm,
            message_area=message_area,
            loading_area=loading_area,
            is_pushed=is_pushed,
        )

    @staticmethod
    def _execute_edit_info_process(action_results: EditInfoActionResults) -> None:
        if not action_results.is_pushed:
            return

        with action_results.loading_area:
            with st_lottie_spinner(animation_source=LoadedLottie.LOADING):
                processers_manager = EditAccountInfoProcesserSState.get()
                processers_manager.run_all(
                    message_area=action_results.message_area,
                    account_id=action_results.account_id,
                    mail_address=action_results.mail_address,
                    family_name_en=action_results.family_name_en,
                    given_name_en=action_results.given_name_en,
                    family_name_jp=action_results.family_name_jp,
                    given_name_jp=action_results.given_name_jp,
                    raw_password=action_results.raw_password,
                )

    @staticmethod
    def _execute_change_pass_process(action_results: ChangePassActionResults) -> None:
        if not action_results.is_pushed:
            return

        with action_results.loading_area:
            with st_lottie_spinner(animation_source=LoadedLottie.LOADING):
                processers_manager = ChangeAccountPassProcesserSState.get()
                processers_manager.run_all(
                    message_area=action_results.message_area,
                    account_id=action_results.account_id,
                    current_raw_password=action_results.current_raw_password,
                    new_raw_password=action_results.new_raw_password,
                    new_raw_password_confirm=action_results.new_raw_password_confirm,
                )

    @classmethod
    def _on_click_return_home(cls):
        MainComponentSState.set_home_entity()
        cls.deinit()

    @classmethod
    def main(cls) -> None:
        cls._display_titles()
        cls._display_return_home_button()

        edit_info_action_results = cls._display_edit_info_form_and_get_results()
        change_pass_action_results = cls._display_change_pass_form_and_get_results()
        cls._execute_edit_info_process(action_results=edit_info_action_results)
        cls._execute_change_pass_process(action_results=change_pass_action_results)

    @staticmethod
    def deinit() -> None:
        EditAccountInfoProcesserSState.deinit()
        ChangeAccountPassProcesserSState.deinit()
