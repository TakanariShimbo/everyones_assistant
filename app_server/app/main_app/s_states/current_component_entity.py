from ...base import BaseSState
from model import MAIN_COMPONENT_TYPE_TABLE, MainComponentTypeEntity


class CurrentComponentEntitySState(BaseSState[MainComponentTypeEntity]):
    @staticmethod
    def get_name() -> str:
        return "CURRENT_COMPONENT_ENTITY"

    @staticmethod
    def get_default() -> MainComponentTypeEntity:
        return MAIN_COMPONENT_TYPE_TABLE.WAKE_UP_ENTITY

    @classmethod
    def set_sign_in_entity(cls) -> None:
        cls.set(value=MAIN_COMPONENT_TYPE_TABLE.SIGN_IN_ENTITY)

    @classmethod
    def set_home_entity(cls) -> None:
        cls.set(value=MAIN_COMPONENT_TYPE_TABLE.HOME_ENTITY)

    @classmethod
    def set_chat_room_entity(cls) -> None:
        cls.set(value=MAIN_COMPONENT_TYPE_TABLE.CHAT_ROOM_ENTITY)

    @classmethod
    def set_account_entity(cls) -> None:
        cls.set(value=MAIN_COMPONENT_TYPE_TABLE.ACCOUNT_ENTITY)
