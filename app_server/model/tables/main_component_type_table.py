from typing import Type

from ..base import BaseTable
from ..configs import MainComponentTypeConfig
from ..beans import MainComponentTypeEntity


class MainComponentTypeTable(BaseTable[MainComponentTypeConfig, MainComponentTypeEntity]):
    @staticmethod
    def _get_config_class() -> Type[MainComponentTypeConfig]:
        return MainComponentTypeConfig

    @staticmethod
    def _get_bean_class() -> Type[MainComponentTypeEntity]:
        return MainComponentTypeEntity

    @property
    def wake_up_entity(self) -> MainComponentTypeEntity:
        return self.get_bean(column_name=MainComponentTypeConfig.get_key_column_name(), value="wake_up")

    @property
    def sign_in_entity(self) -> MainComponentTypeEntity:
        return self.get_bean(column_name=MainComponentTypeConfig.get_key_column_name(), value="sign_in")

    @property
    def home_entity(self) -> MainComponentTypeEntity:
        return self.get_bean(column_name=MainComponentTypeConfig.get_key_column_name(), value="home")

    @property
    def chat_room_entity(self) -> MainComponentTypeEntity:
        return self.get_bean(column_name=MainComponentTypeConfig.get_key_column_name(), value="chat_room")


MAIN_COMPONENT_TYPE_TABLE = MainComponentTypeTable.load_from_csv()
