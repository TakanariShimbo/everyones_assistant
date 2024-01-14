from typing import Type

from ..base import BaseTable
from ..configs import RoleTypeConfig
from ..beans import RoleTypeEntity


class RoleTypeTable(BaseTable[RoleTypeConfig, RoleTypeEntity]):
    @staticmethod
    def _get_config_class() -> Type[RoleTypeConfig]:
        return RoleTypeConfig
    
    @staticmethod
    def _get_bean_class() -> Type[RoleTypeEntity]:
        return RoleTypeEntity

    @property
    def system_id(self) -> str:
        return self.get_bean(column_name=RoleTypeConfig.get_key_column_name(), value="system").role_id

    @property
    def user_id(self) -> str:
        return self.get_bean(column_name=RoleTypeConfig.get_key_column_name(), value="user").role_id
    
    @property
    def assistant_id(self) -> str:
        return self.get_bean(column_name=RoleTypeConfig.get_key_column_name(), value="assistant").role_id


ROLE_TYPE_TABLE = RoleTypeTable.load_from_csv()
