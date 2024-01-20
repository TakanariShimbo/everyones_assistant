from ..base import BasePage
from .s_states import CurrentComponentEntitySState
from .components import WakeupComponent, SignInComponent, HomeComponent, ChatRoomComponent, AccountComponent
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
        CurrentComponentEntitySState.init()

    @staticmethod
    def main() -> None:
        current_component_entity = CurrentComponentEntitySState.get()
        if current_component_entity == MAIN_COMPONENT_TYPE_TABLE.WAKE_UP_ENTITY:
            WakeupComponent.run()
        elif current_component_entity == MAIN_COMPONENT_TYPE_TABLE.SIGN_IN_ENTITY:
            SignInComponent.run()
        elif current_component_entity == MAIN_COMPONENT_TYPE_TABLE.HOME_ENTITY:
            HomeComponent.run()
        elif current_component_entity == MAIN_COMPONENT_TYPE_TABLE.CHAT_ROOM_ENTITY:
            ChatRoomComponent.run()
        elif current_component_entity == MAIN_COMPONENT_TYPE_TABLE.ACCOUNT_ENTITY:
            AccountComponent.run()
        else:
            raise ValueError("ComponentSState Value Error")
