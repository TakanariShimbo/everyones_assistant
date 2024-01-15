from typing import Type

from ..base import BaseCsvTable
from ..configs import MainComponentTypeConfig, MainComponentTypeColumnConfigs
from ..beans import MainComponentTypeEntity


class MainComponentTypeTable(BaseCsvTable[MainComponentTypeConfig, MainComponentTypeEntity]):
    @staticmethod
    def _get_config_class() -> Type[MainComponentTypeConfig]:
        return MainComponentTypeConfig

    @staticmethod
    def _get_bean_class() -> Type[MainComponentTypeEntity]:
        return MainComponentTypeEntity

    @property
    def WAKE_UP_ENTITY(self) -> MainComponentTypeEntity:
        return self.get_bean(column_name=MainComponentTypeColumnConfigs.get_key_column_name(), value="wake_up")

    @property
    def SIGN_IN_ENTITY(self) -> MainComponentTypeEntity:
        return self.get_bean(column_name=MainComponentTypeColumnConfigs.get_key_column_name(), value="sign_in")

    @property
    def HOME_ENTITY(self) -> MainComponentTypeEntity:
        return self.get_bean(column_name=MainComponentTypeColumnConfigs.get_key_column_name(), value="home")

    @property
    def CHAT_ROOM_ENTITY(self) -> MainComponentTypeEntity:
        return self.get_bean(column_name=MainComponentTypeColumnConfigs.get_key_column_name(), value="chat_room")


MAIN_COMPONENT_TYPE_TABLE = MainComponentTypeTable.load_from_csv()
