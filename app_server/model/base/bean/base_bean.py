from abc import ABC, abstractmethod
from typing import Any, Dict, List, Generic, TypeVar, Type, Union

import pandas as pd
from pandas.api.extensions import ExtensionDtype

from ..column_config import ColumnConfig
from ..config import BaseConfig


C = TypeVar("C", bound=BaseConfig)
B = TypeVar("B", bound="BaseBean")


class BaseBean(Generic[C], ABC):
    @staticmethod
    @abstractmethod
    def _get_config_class() -> Type[C]:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def _check_is_same(self, other: Any) -> bool:
        raise NotImplementedError("Subclasses must implement this method")

    @classmethod
    def _get_column_configs(cls) -> List[ColumnConfig]:
        return cls._get_config_class()._get_column_configs()

    @classmethod
    def _get_column_names(cls, ignore_auto_assigned: bool) -> List[str]:
        return cls._get_config_class()._get_column_names(ignore_auto_assigned=ignore_auto_assigned)

    @classmethod
    def _get_dtype_dict(cls) -> Dict[str, ExtensionDtype]:
        return cls._get_config_class()._get_dtype_dict()

    def __eq__(self, other):
        return self._check_is_same(other=other)

    @classmethod
    def init_from_dict(cls: Type[B], bean_dict: Union[Dict[str, Any], pd.Series]) -> B:
        kwargs = {name: None if pd.isna(bean_dict[name]) else bean_dict[name] for name in cls._get_column_names(ignore_auto_assigned=False)}
        return cls(**kwargs)

    def to_dict(self, ignore_auto_assigned: bool) -> Dict[str, Any]:
        bean_dict = {}
        for name in self._get_column_names(ignore_auto_assigned=ignore_auto_assigned):
            try:
                bean_dict[name] = getattr(self, name)
            except ValueError:
                bean_dict[name] = None
        return bean_dict
