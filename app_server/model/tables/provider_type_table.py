from typing import Type

from ..base import BaseCsvTable
from ..configs import ProviderTypeConfig
from ..beans import ProviderTypeEntity


class ProviderTypeTable(BaseCsvTable[ProviderTypeConfig, ProviderTypeEntity]):
    @staticmethod
    def _get_config_class() -> Type[ProviderTypeConfig]:
        return ProviderTypeConfig
    
    @staticmethod
    def _get_bean_class() -> Type[ProviderTypeEntity]:
        return ProviderTypeEntity

    @property
    def open_ai_id(self) -> str:
        return self.get_bean(column_name=ProviderTypeConfig.get_key_column_name(), value="open-ai").provider_id

    @property
    def google_id(self) -> str:
        return self.get_bean(column_name=ProviderTypeConfig.get_key_column_name(), value="google").provider_id


PROVIDER_TYPE_TABLE = ProviderTypeTable.load_from_csv()
