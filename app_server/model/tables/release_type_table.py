from typing import Type

from ..base import BaseCsvTable
from ..configs import ReleaseTypeConfig, ReleaseTypeColumnConfigs
from ..beans import ReleaseTypeEntity


class ReleaseTypeTable(BaseCsvTable[ReleaseTypeConfig, ReleaseTypeEntity]):
    @staticmethod
    def _get_config_class() -> Type[ReleaseTypeConfig]:
        return ReleaseTypeConfig
    
    @staticmethod
    def _get_bean_class() -> Type[ReleaseTypeEntity]:
        return ReleaseTypeEntity

    @property
    def PUBLIC_ID(self) -> str:
        return self.get_bean(column_name=ReleaseTypeColumnConfigs.get_key_column_name(), value="public").release_id

    @property
    def PRIVATE_ID(self) -> str:
        return self.get_bean(column_name=ReleaseTypeColumnConfigs.get_key_column_name(), value="private").release_id


RELEASE_TYPE_TABLE = ReleaseTypeTable.load_from_csv()
