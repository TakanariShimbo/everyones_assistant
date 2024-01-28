from time import sleep

import streamlit as st
from streamlit_lottie import st_lottie

from ...base import BaseComponent
from .. import s_states as SStates
from .. import q_params as QParams
from model import LoadedLottie


class WakeupComponent(BaseComponent):
    @staticmethod
    def init() -> None:
        SStates.CurrentComponentEntity.init()
        QParams.ComponentId.set(value=SStates.CurrentComponentEntity.get().component_id)

    @classmethod
    def main(cls) -> None:
        st_lottie(animation_source=LoadedLottie.WAKE_UP_LOGO, speed=1.2, reverse=False, loop=False)
        sleep(4)
        SStates.CurrentComponentEntity.set_sign_in_entity()
        st.rerun()

    @staticmethod
    def deinit() -> None:
        pass
