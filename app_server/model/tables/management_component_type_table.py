from typing import Type

from ..base import BaseCsvTable
from ..configs import ManagementComponentTypeConfig
from ..beans import ManagementComponentTypeEntity


class ManagementComponentTypeTable(BaseCsvTable[ManagementComponentTypeConfig, ManagementComponentTypeEntity]):
    @staticmethod
    def _get_config_class() -> Type[ManagementComponentTypeConfig]:
        return ManagementComponentTypeConfig

    @staticmethod
    def _get_bean_class() -> Type[ManagementComponentTypeEntity]:
        return ManagementComponentTypeEntity

    @property
    def sign_in_entity(self) -> ManagementComponentTypeEntity:
        return self.get_bean(column_name=ManagementComponentTypeConfig.get_key_column_name(), value="sign_in")

    @property
    def home_entity(self) -> ManagementComponentTypeEntity:
        return self.get_bean(column_name=ManagementComponentTypeConfig.get_key_column_name(), value="home")

    @property
    def sign_up_entity(self) -> ManagementComponentTypeEntity:
        return self.get_bean(column_name=ManagementComponentTypeConfig.get_key_column_name(), value="sign_up")


MANAGEMENT_COMPONENT_TYPE_TABLE = ManagementComponentTypeTable.load_from_csv()
