from textwrap import dedent

import streamlit as st

from ...base import BaseComponent
from ..management_s_states import ManagementComponentSState


class HomeComponent(BaseComponent):
    @staticmethod
    def init() -> None:
        pass

    @staticmethod
    def _display_titles() -> None:
        current_component_entity = ManagementComponentSState.get()
        st.markdown(f"### {current_component_entity.label_en}")
        st.sidebar.markdown("## Menes")

    @classmethod
    def _display_sign_out_button(cls) -> None:
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

    @classmethod
    def _display_accounts(cls) -> None:
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
                st.button(label="Enter", type="primary", on_click=cls._on_click_accounts, use_container_width=True)

    @classmethod
    def _on_click_sign_out(cls) -> None:
        ManagementComponentSState.set_sign_in_entity()
        cls.deinit()

    @classmethod
    def _on_click_accounts(cls) -> None:
        ManagementComponentSState.set_accounts_entity()
        cls.deinit()

    @classmethod
    def main(cls) -> None:
        cls._display_titles()
        cls._display_sign_out_button()
        cls._display_overview()
        cls._display_accounts()

    @staticmethod
    def deinit() -> None:
        pass
