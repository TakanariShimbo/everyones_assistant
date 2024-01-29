from ..base import BasePage
from . import s_states as SStates
from . import q_params as QParams
from . import components as Components
from model import MAIN_COMPONENT_TYPE_TABLE


class MainPage(BasePage):
    @staticmethod
    def get_title() -> str:
        return "Everyone's Assistant"

    @staticmethod
    def get_icon() -> str:
        return "🧠"

    @staticmethod
    def init() -> None:
        SStates.CurrentComponentEntity.init()
        QParams.ComponentId.set(value=SStates.CurrentComponentEntity.get().component_id)

    @staticmethod
    def main() -> None:
        current_component_entity = SStates.CurrentComponentEntity.get()
        if current_component_entity == MAIN_COMPONENT_TYPE_TABLE.WAKE_UP_ENTITY:
            Components.WakeupComponent.run()
        elif current_component_entity == MAIN_COMPONENT_TYPE_TABLE.SIGN_IN_ENTITY:
            Components.SignInComponent.run()
        elif current_component_entity == MAIN_COMPONENT_TYPE_TABLE.HOME_ENTITY:
            Components.HomeComponent.run()
        elif current_component_entity == MAIN_COMPONENT_TYPE_TABLE.CHAT_ROOM_ENTITY:
            Components.ChatRoomComponent.run()
        elif current_component_entity == MAIN_COMPONENT_TYPE_TABLE.ACCOUNT_ENTITY:
            Components.AccountComponent.run()
        else:
            raise ValueError("ComponentSState Value Error")
