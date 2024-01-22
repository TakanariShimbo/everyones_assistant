from ...base import BaseSStateHasDefault
from model import MANAGEMENT_COMPONENT_TYPE_TABLE, ManagementComponentTypeEntity


class CurrentComponentEntity(BaseSStateHasDefault[ManagementComponentTypeEntity]):
    @staticmethod
    def get_name() -> str:
        return "CURRENT_COMPONENT_ENTITY"

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
    def set_accounts_entity(cls):
        cls.set(value=MANAGEMENT_COMPONENT_TYPE_TABLE.ACCOUNTS_ENTITY)
