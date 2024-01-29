import streamlit as st
from streamlit_lottie import st_lottie_spinner

from ...base import BaseComponent
from .. import s_states as SStates
from ..pre_components.home import HomePreComponent
from ..action_results.accounts import SignUpActionResults, UpdateInformationActionResults
from model import LoadedLottie, LoadedImage


class AccountsComponent(BaseComponent):
    @staticmethod
    def init() -> None:
        SStates.LoadedAccountTable.validate()
        SStates.CurrentComponentEntity.init()
        SStates.SignUpProcess.init()
        SStates.EditAccountTableProcess.init()
        SStates.LoadAccountTableProcess.init()
        SStates.AccountsDataEditorKey.init()
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

            left_area, right_area = st.columns([1, 1])
            with left_area:
                is_user = st.toggle(
                    label="User Authority",
                    value=True,
                    key="UserAuthorityToggle",
                )
            with right_area:
                is_administrator = st.toggle(
                    label="Administrator Authority",
                    value=False,
                    key="AdministratorAuthorityToggle",
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
            is_user=is_user,
            is_administrator=is_administrator,
            message_area=message_area,
            loading_area=loading_area,
            is_pushed=is_pushed,
        )

    @staticmethod
    def _display_account_table_and_get_results() -> UpdateInformationActionResults:
        st.markdown("#### 📝 Update Informatin")
        with st.form(key="UpdateInformatinAccountsForm", border=True):
            account_table = SStates.LoadedAccountTable.get()
            edited_display_df = st.data_editor(
                data=account_table.display_df,
                disabled=account_table.uneditable_columns,
                hide_index=True, 
                use_container_width=True,
                key=f"AccountTableDataEditor{SStates.AccountsDataEditorKey.get()}",
            )

            _, update_button_area, _, load_button_area, _ = st.columns([2, 3, 2, 3, 2])
            with update_button_area:
                is_update_pushed = st.form_submit_button(label="Update", type="primary", use_container_width=True)
            with load_button_area:
                is_load_pushed = st.form_submit_button(label="Load", type="secondary", use_container_width=True)

            _, loading_area, _ = st.columns([1, 1, 1])

        return UpdateInformationActionResults(
            loading_area=loading_area,
            is_update_pushed=is_update_pushed,
            is_load_pushed=is_load_pushed,
            edited_display_df=edited_display_df,
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
                    is_user=action_results.is_user,
                    is_administrator=action_results.is_administrator,
                )

        if not response.is_success:
            action_results.message_area.warning(response.message)
            return False

        action_results.message_area.success(response.message)
        return True

    @staticmethod
    def _execute_update_information_process(action_results: UpdateInformationActionResults) -> bool:
        if not action_results.is_update_pushed and not action_results.is_load_pushed:
            return False

        with action_results.loading_area:
            with st_lottie_spinner(animation_source=LoadedLottie.LOADING):
                if action_results.is_update_pushed:
                    processer_manager = SStates.EditAccountTableProcess.get()
                    processer_manager.run_all(edited_display_df=action_results.edited_display_df)                
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
        update_information_action_results = cls._display_account_table_and_get_results()
        
        cls._execute_sign_up_process(action_results=sign_up_action_results)
        is_success = cls._execute_update_information_process(action_results=update_information_action_results)
        if is_success:
            cls.deinit()
            st.rerun()

    @staticmethod
    def deinit() -> None:
        SStates.SignUpProcess.deinit()
        SStates.EditAccountTableProcess.deinit()
        SStates.LoadAccountTableProcess.deinit()
        SStates.LoadedAccountTable.deinit()
        SStates.AccountsDataEditorKey.deinit()
        HomePreComponent.deinit()
