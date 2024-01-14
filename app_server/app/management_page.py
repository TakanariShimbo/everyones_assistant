from .base import BasePage
from .management_s_states import ManagementComponentSState
from .management_components import SignInComponent, HomeComponent, SignUpComponent
from model import MANAGEMENT_COMPONENT_TYPE_TABLE


class ManagementPage(BasePage):
    @staticmethod
    def get_title() -> str:
        return "Management Everyone's Assistant"

    @staticmethod
    def get_icon() -> str:
        return "🧠"

    @staticmethod
    def init() -> None:
        ManagementComponentSState.init()

    @staticmethod
    def main() -> None:
        current_component_entity = ManagementComponentSState.get()
        if current_component_entity == MANAGEMENT_COMPONENT_TYPE_TABLE.sign_in_entity:
            SignInComponent.run()
        elif current_component_entity == MANAGEMENT_COMPONENT_TYPE_TABLE.home_entity:
            HomeComponent.run()
        elif current_component_entity == MANAGEMENT_COMPONENT_TYPE_TABLE.sign_up_entity:
            SignUpComponent.run()
        else:
            raise ValueError("ComponentSState Value Error")
