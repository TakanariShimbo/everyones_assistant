from abc import ABC, abstractmethod
from typing import Dict, List

from pandas.api.extensions import ExtensionDtype

from .. import ColumnConfig


class BaseConfig(ABC):
    @staticmethod
    @abstractmethod
    def _get_column_configs() -> List[ColumnConfig]:
        raise NotImplementedError("Subclasses must implement this method")

    @classmethod
    def _get_column_names(cls, ignore_auto_assigned: bool) -> List[str]:
        if ignore_auto_assigned:
            return [config.name for config in cls._get_column_configs() if not config.auto_assigned]
        else:
            return [config.name for config in cls._get_column_configs()]

    @classmethod
    def _get_dtype_dict(cls) -> Dict[str, ExtensionDtype]:
        return {config.name: config.dtype for config in cls._get_column_configs()}
