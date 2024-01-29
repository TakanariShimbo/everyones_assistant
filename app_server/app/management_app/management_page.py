from ..base import BasePage
from . import s_states as SStates
from . import q_params as QParams
from . import components as Components
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
        SStates.CurrentComponentEntity.init()
        QParams.ComponentId.set(value=SStates.CurrentComponentEntity.get().component_id)

    @staticmethod
    def main() -> None:
        current_component_entity = SStates.CurrentComponentEntity.get()
        if current_component_entity == MANAGEMENT_COMPONENT_TYPE_TABLE.SIGN_IN_ENTITY:
            Components.SignInComponent.run()
        elif current_component_entity == MANAGEMENT_COMPONENT_TYPE_TABLE.HOME_ENTITY:
            Components.HomeComponent.run()
        elif current_component_entity == MANAGEMENT_COMPONENT_TYPE_TABLE.ACCOUNTS_ENTITY:
            Components.AccountsComponent.run()
        else:
            raise ValueError("ComponentSState Value Error")
