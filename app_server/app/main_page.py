from .base import BasePage
from .main_s_states import MainComponentSState
from .main_components import WakeupComponent, SignInComponent, HomeComponent, ChatRoomComponent, AccountsComponent
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
        MainComponentSState.init()

    @staticmethod
    def main() -> None:
        current_component_entity = MainComponentSState.get()
        if current_component_entity == MAIN_COMPONENT_TYPE_TABLE.WAKE_UP_ENTITY:
            WakeupComponent.run()
        elif current_component_entity == MAIN_COMPONENT_TYPE_TABLE.SIGN_IN_ENTITY:
            SignInComponent.run()
        elif current_component_entity == MAIN_COMPONENT_TYPE_TABLE.HOME_ENTITY:
            HomeComponent.run()
        elif current_component_entity == MAIN_COMPONENT_TYPE_TABLE.CHAT_ROOM_ENTITY:
            ChatRoomComponent.run()
        elif current_component_entity == MAIN_COMPONENT_TYPE_TABLE.ACCOUNTS_ENTITY:
            AccountsComponent.run()
        else:
            raise ValueError("ComponentSState Value Error")
