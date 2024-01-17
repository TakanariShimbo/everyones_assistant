from .base import BasePage
from .management_s_states import ManagementComponentSState
from .management_components import SignInComponent, HomeComponent, AccountsComponent
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
        if current_component_entity == MANAGEMENT_COMPONENT_TYPE_TABLE.SIGN_IN_ENTITY:
            SignInComponent.run()
        elif current_component_entity == MANAGEMENT_COMPONENT_TYPE_TABLE.HOME_ENTITY:
            HomeComponent.run()
        elif current_component_entity == MANAGEMENT_COMPONENT_TYPE_TABLE.ACCOUNTS_ENTITY:
            AccountsComponent.run()
        else:
            raise ValueError("ComponentSState Value Error")
