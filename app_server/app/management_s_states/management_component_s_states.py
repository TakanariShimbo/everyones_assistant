from ..base import BaseSState
from model import MANAGEMENT_COMPONENT_TYPE_TABLE, ManagementComponentTypeEntity


class ManagementComponentSState(BaseSState[ManagementComponentTypeEntity]):
    @staticmethod
    def get_name() -> str:
        return "ACTIVE_MANAGEMENT_COMPONENT"

    @staticmethod
    def get_default() -> ManagementComponentTypeEntity:
        return MANAGEMENT_COMPONENT_TYPE_TABLE.SIGN_IN_ENTITY

    @classmethod
    def set_sign_in_entity(cls):
        cls.set(value=MANAGEMENT_COMPONENT_TYPE_TABLE.SIGN_IN_ENTITY)

    @classmethod
    def set_home_entity(cls):
        cls.set(value=MANAGEMENT_COMPONENT_TYPE_TABLE.HOME_ENTITY)

    @classmethod
    def set_sign_up_entity(cls):
        cls.set(value=MANAGEMENT_COMPONENT_TYPE_TABLE.SIGN_UP_ENTITY)
