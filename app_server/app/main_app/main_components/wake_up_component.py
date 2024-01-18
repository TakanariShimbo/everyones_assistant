from time import sleep

import streamlit as st
from streamlit_lottie import st_lottie

from ...base import BaseComponent
from ..main_s_states import MainComponentSState
from model import LoadedLottie


class WakeupComponent(BaseComponent):
    @staticmethod
    def init() -> None:
        pass

    @classmethod
    def main(cls) -> None:
        st_lottie(animation_source=LoadedLottie.WAKE_UP_LOGO, speed=1.2, reverse=False, loop=False)
        sleep(4)
        MainComponentSState.set_sign_in_entity()
        st.rerun()

    @staticmethod
    def deinit() -> None:
        pass
