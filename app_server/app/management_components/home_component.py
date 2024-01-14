from textwrap import dedent

import streamlit as st

from ..base import BaseComponent
from ..management_s_states import ManagementComponentSState


class HomeComponent(BaseComponent):
    @staticmethod
    def init() -> None:
        pass

    @classmethod
    def _display_sign_out_button(cls) -> None:
        st.sidebar.button(label="👤 Sign out", key="SignOutButton", on_click=cls._on_click_sign_out, use_container_width=True)

    @classmethod
    def _display_sign_up_button(cls) -> None:
        st.sidebar.button(label="➕ Sign up", key="SignUpButton", on_click=cls._on_click_sign_up, use_container_width=True)

    @staticmethod
    def _display_title() -> None:
        current_component_entity = ManagementComponentSState.get()
        st.markdown(f"### {current_component_entity.label_en}")

    @staticmethod
    def _display_overview() -> None:
        content = dedent(
            f"""
            #### 🔎 Overview
            Welcome to Management Everyone's Assistant.   
            Experience the forefront of AI technology and explore the possibilities of the future.  
            AI makes your daily life smarter and easier.  
            """
        )
        st.markdown(content)

    @classmethod
    def _on_click_sign_out(cls) -> None:
        ManagementComponentSState.set_sign_in_entity()
        cls.deinit()

    @classmethod
    def _on_click_sign_up(cls) -> None:
        ManagementComponentSState.set_sign_up_entity()
        cls.deinit()

    @classmethod
    def main(cls) -> None:
        cls._display_sign_out_button()
        cls._display_sign_up_button()
        cls._display_title()
        cls._display_overview()

    @staticmethod
    def deinit() -> None:
        pass
