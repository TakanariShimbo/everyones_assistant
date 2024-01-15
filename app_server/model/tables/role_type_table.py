from typing import Type

from ..base import BaseCsvTable
from ..configs import RoleTypeConfig, RoleTypeColumnConfigs
from ..beans import RoleTypeEntity


class RoleTypeTable(BaseCsvTable[RoleTypeConfig, RoleTypeEntity]):
    @staticmethod
    def _get_config_class() -> Type[RoleTypeConfig]:
        return RoleTypeConfig
    
    @staticmethod
    def _get_bean_class() -> Type[RoleTypeEntity]:
        return RoleTypeEntity

    @property
    def SYSTEM_ID(self) -> str:
        return self.get_bean(column_name=RoleTypeColumnConfigs.get_key_column_name(), value="system").role_id

    @property
    def USER_ID(self) -> str:
        return self.get_bean(column_name=RoleTypeColumnConfigs.get_key_column_name(), value="user").role_id
    
    @property
    def ASSISTANT_ID(self) -> str:
        return self.get_bean(column_name=RoleTypeColumnConfigs.get_key_column_name(), value="assistant").role_id


ROLE_TYPE_TABLE = RoleTypeTable.load_from_csv()
