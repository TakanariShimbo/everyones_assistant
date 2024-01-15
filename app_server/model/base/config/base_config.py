from abc import ABC, abstractmethod
from typing import Dict, List

from pandas.api.extensions import ExtensionDtype

from .. import ColumnConfig, BaseColumnConfigEnum


class BaseConfig(ABC):
    @staticmethod
    @abstractmethod
    def _get_column_configs() -> BaseColumnConfigEnum:
        raise NotImplementedError("Subclasses must implement this method")

    @classmethod
    def _get_column_config_list(cls) -> List[ColumnConfig]:
        return cls._get_column_configs().to_list()

    @classmethod
    def _get_column_names(cls, ignore_auto_assigned: bool) -> List[str]:
        if ignore_auto_assigned:
            return [config.name for config in cls._get_column_config_list() if not config.auto_assigned]
        else:
            return [config.name for config in cls._get_column_config_list()]

    @classmethod
    def _get_dtype_dict(cls) -> Dict[str, ExtensionDtype]:
        return {config.name: config.dtype for config in cls._get_column_config_list()}

    @classmethod
    def get_key_column_name(cls) -> str:
        return cls._get_column_config_list()[0].name