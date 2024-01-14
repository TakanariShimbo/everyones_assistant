from ..base import BaseSState
from model import MAIN_COMPONENT_TYPE_TABLE, MainComponentTypeEntity


class MainComponentSState(BaseSState[MainComponentTypeEntity]):
    @staticmethod
    def get_name() -> str:
        return "ACTIVE_MAIN_COMPONENT"

    @staticmethod
    def get_default() -> MainComponentTypeEntity:
        return MAIN_COMPONENT_TYPE_TABLE.wake_up_entity

    @classmethod
    def set_sign_in_entity(cls):
        cls.set(value=MAIN_COMPONENT_TYPE_TABLE.sign_in_entity)

    @classmethod
    def set_home_entity(cls):
        cls.set(value=MAIN_COMPONENT_TYPE_TABLE.home_entity)

    @classmethod
    def set_chat_room_entity(cls):
        cls.set(value=MAIN_COMPONENT_TYPE_TABLE.chat_room_entity)
