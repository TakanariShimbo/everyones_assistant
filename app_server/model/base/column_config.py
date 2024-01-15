from enum import Enum
from typing import List

from pandas.api.extensions import ExtensionDtype


class ColumnConfig:
    def __init__(
        self,
        name: str,
        dtype: ExtensionDtype,
        unique: bool = False,
        non_null: bool = False,
        auto_assigned: bool = False,
    ):
        self._name = name
        self._dtype = dtype
        self._unique = unique
        self._non_null = non_null
        self._auto_assigned = auto_assigned

    @property
    def name(self) -> str:
        return self._name

    @property
    def dtype(self) -> ExtensionDtype:
        return self._dtype

    @property
    def unique(self) -> bool:
        return self._unique

    @property
    def non_null(self) -> bool:
        return self._non_null

    @property
    def auto_assigned(self) -> bool:
        return self._auto_assigned


class BaseColumnConfigEnum(ColumnConfig, Enum):
    @classmethod
    def to_list(cls) -> List[ColumnConfig]:
        return [config.value for config in cls]

    @classmethod
    def get_key_column_name(cls) -> str:
        return cls.to_list()[0].name