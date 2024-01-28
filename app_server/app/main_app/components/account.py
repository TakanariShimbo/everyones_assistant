import streamlit as st
from streamlit_lottie import st_lottie_spinner

from ...base import BaseComponent
from .. import s_states as SStates
from .. import q_params as QParams
from ..pre_components.home import HomePreComponent
from ..action_results.account import UpdateInfoActionResults, ChangePassActionResults, ReturnHomeActionResults
from model import LoadedLottie, LoadedImage


class AccountComponent(BaseComponent):
    @staticmethod
    def init() -> None:
        SStates.SignedInAccountEntity.validate()
        SStates.CurrentComponentEntity.init()
        QParams.ComponentId.set(value=SStates.CurrentComponentEntity.get().component_id)
        SStates.UpdateAccountInfoProcess.init()
        SStates.ChangeAccountPassProcess.init()
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
    def _display_update_info_form_and_get_results() -> UpdateInfoActionResults:
        signed_in_account_entity = SStates.SignedInAccountEntity.get()

        st.markdown("#### 📝 Update Information")
        with st.form(key="UpdateInfoForm", border=True):
            left_area, right_area = st.columns([1, 1])
            with left_area:
                st.text_input(
                    label="Account ID",
                    placeholder="Enter account id here.",
                    key="AccountIdTextInput",
                    value=signed_in_account_entity.account_id,
                    disabled=True,
                )
            with right_area:
                inputed_mail_address = st.text_input(
                    label="Email Address",
                    placeholder="Enter your email here.",
                    key="MailAddressTextInput",
                    value=signed_in_account_entity.mail_address,
                )

            left_area, right_area = st.columns([1, 1])
            with left_area:
                inputed_family_name_en = st.text_input(
                    label="Family Name (English)",
                    placeholder="Enter your family name in English here.",
                    key="FamilyNameEnTextInput",
                    value=signed_in_account_entity.family_name_en,
                )
            with right_area:
                inputed_given_name_en = st.text_input(
                    label="Given Name (English)",
                    placeholder="Enter your given name in English here.",
                    key="GivenNameEnTextInput",
                    value=signed_in_account_entity.given_name_en,
                )

            left_area, right_area = st.columns([1, 1])
            with left_area:
                inputed_family_name_jp = st.text_input(
                    label="Family Name (Japanese)",
                    placeholder="Enter your family name in Japanese here.",
                    key="FamilyNameJpTextInput",
                    value=signed_in_account_entity.family_name_jp,
                )
            with right_area:
                inputed_given_name_jp = st.text_input(
                    label="Given Name (Japanese)",
                    placeholder="Enter your given name in Japanese here.",
                    key="GivenNameJpTextInput",
                    value=signed_in_account_entity.given_name_jp,
                )

            inputed_raw_password = st.text_input(
                label="Current Password",
                placeholder="Enter password here.",
                key="PasswordTextInput",
                type="password",
            )

            message_area = st.empty()
            _, button_area, _ = st.columns([5, 3, 5])
            with button_area:
                is_pushed = st.form_submit_button(label="Update", type="primary", use_container_width=True)
            _, loading_area, _ = st.columns([1, 1, 1])

        return UpdateInfoActionResults(
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
        st.markdown("#### 🔑 Change Password")
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
            current_raw_password=inputed_current_raw_password,
            new_raw_password=inputed_new_raw_password,
            new_raw_password_confirm=inputed_new_raw_password_confirm,
            message_area=message_area,
            loading_area=loading_area,
            is_pushed=is_pushed,
        )

    @staticmethod
    def _execute_update_info_process(action_results: UpdateInfoActionResults) -> None:
        if not action_results.is_pushed:
            return

        with action_results.loading_area:
            with st_lottie_spinner(animation_source=LoadedLottie.LOADING):
                processer_manager = SStates.UpdateAccountInfoProcess.get()
                response = processer_manager.run_all(
                    message_area=action_results.message_area,
                    mail_address=action_results.mail_address,
                    family_name_en=action_results.family_name_en,
                    given_name_en=action_results.given_name_en,
                    family_name_jp=action_results.family_name_jp,
                    given_name_jp=action_results.given_name_jp,
                    raw_password=action_results.raw_password,
                )

        if not response.is_success:
            action_results.message_area.warning(response.message)
            return

        action_results.message_area.success(response.message)

    @staticmethod
    def _execute_return_home_process(action_results: ReturnHomeActionResults) -> bool:
        if not action_results.is_pushed:
            return False

        with action_results.loading_area:
            with st_lottie_spinner(animation_source=LoadedLottie.LOADING):
                HomePreComponent.prepare()
        return True

    @staticmethod
    def _execute_change_pass_process(action_results: ChangePassActionResults) -> None:
        if not action_results.is_pushed:
            return

        with action_results.loading_area:
            with st_lottie_spinner(animation_source=LoadedLottie.LOADING):
                processer_manager = SStates.ChangeAccountPassProcess.get()
                response = processer_manager.run_all(
                    message_area=action_results.message_area,
                    current_raw_password=action_results.current_raw_password,
                    new_raw_password=action_results.new_raw_password,
                    new_raw_password_confirm=action_results.new_raw_password_confirm,
                )

        if not response.is_success:
            action_results.message_area.warning(response.message)
            return

        action_results.message_area.success(response.message)

    @classmethod
    def main(cls) -> None:
        cls._display_titles()
        return_home_action_results = cls._display_sidebar_titles_and_get_results()
        update_info_action_results = cls._display_update_info_form_and_get_results()
        change_pass_action_results = cls._display_change_pass_form_and_get_results()

        is_success = cls._execute_return_home_process(action_results=return_home_action_results)
        if is_success:
            cls.deinit()
            st.rerun()
        cls._execute_update_info_process(action_results=update_info_action_results)
        cls._execute_change_pass_process(action_results=change_pass_action_results)

    @staticmethod
    def deinit() -> None:
        SStates.UpdateAccountInfoProcess.deinit()
        SStates.ChangeAccountPassProcess.deinit()
        HomePreComponent.deinit()
