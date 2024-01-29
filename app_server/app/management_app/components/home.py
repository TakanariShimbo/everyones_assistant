from textwrap import dedent

import streamlit as st
from streamlit_lottie import st_lottie_spinner

from ...base import BaseComponent
from .. import s_states as SStates
from ..pre_components.sign_in import SignInPreComponent
from ..pre_components.accounts import AccountsPreComponent
from ..action_results.home import ActionResults
from model import LoadedImage, LoadedLottie


class HomeComponent(BaseComponent):
    @staticmethod
    def init() -> None:
        SStates.CurrentComponentEntity.init()
        SignInPreComponent.init()
        AccountsPreComponent.init()

    @staticmethod
    def _display_titles() -> None:
        current_component_entity = SStates.CurrentComponentEntity.get()
        st.markdown(f"### {current_component_entity.label_en}")

    @classmethod
    def _display_sidebar_titles(cls) -> None:
        st.sidebar.image(image=LoadedImage.LOGO, use_column_width=True)
        st.sidebar.button(label="🚪 Sign out", key="SignOutButton", on_click=cls._on_click_sign_out, use_container_width=True)

    @staticmethod
    def _display_overview() -> None:
        st.markdown("#### 🔎 Overview")
        with st.container(border=True):
            content = dedent(
                f"""
                Welcome to Management Everyone's Assistant.   
                Experience the forefront of AI technology and explore the possibilities of the future.  
                AI makes your daily life smarter and easier.  
                """
            )
            st.markdown(content)

    @staticmethod
    def _display_accounts_and_get_results() -> ActionResults:
        st.markdown("#### 👤 Accounts")
        with st.container(border=True):
            content = dedent(
                f"""
                You can easily oversee and manage multiple user accounts.   
                Here, you can update profiles, adjust privacy settings with just a few clicks.   
                Offering a secure and efficient experience.
                """
            )
            st.markdown(content)
            _, button_area, _ = st.columns([5, 3, 5])
            with button_area:
                is_pushed = st.button(label="Enter", type="primary", use_container_width=True)
            _, loading_area, _ = st.columns([1, 1, 1])
        return ActionResults(loading_area=loading_area, is_pushed=is_pushed)

    @staticmethod
    def _execute_accounts_pre_process(action_results: ActionResults) -> bool:
        if not action_results.is_pushed:
            return False

        with action_results.loading_area:
            with st_lottie_spinner(animation_source=LoadedLottie.LOADING):
                AccountsPreComponent.prepare()
        return True

    @classmethod
    def _on_click_sign_out(cls) -> None:
        SignInPreComponent.prepare()
        cls.deinit()

    @classmethod
    def main(cls) -> None:
        cls._display_titles()
        cls._display_sidebar_titles()
        cls._display_overview()
        action_results = cls._display_accounts_and_get_results()
        is_success = cls._execute_accounts_pre_process(action_results=action_results)
        if is_success:
            cls.deinit()
            st.rerun()

    @staticmethod
    def deinit() -> None:
        SignInPreComponent.deinit()
        AccountsPreComponent.deinit()
