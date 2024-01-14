from .base import BasePage
from .main_s_states import MainComponentSState
from .main_components import WakeupComponent, SignInComponent, HomeComponent, ChatRoomComponent
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
        if current_component_entity == MAIN_COMPONENT_TYPE_TABLE.wake_up_entity:
            WakeupComponent.run()
        elif current_component_entity == MAIN_COMPONENT_TYPE_TABLE.sign_in_entity:
            SignInComponent.run()
        elif current_component_entity == MAIN_COMPONENT_TYPE_TABLE.home_entity:
            HomeComponent.run()
        elif current_component_entity == MAIN_COMPONENT_TYPE_TABLE.chat_room_entity:
            ChatRoomComponent.run()
        else:
            raise ValueError("ComponentSState Value Error")
