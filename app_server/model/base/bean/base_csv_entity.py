from abc import ABC
from typing import TypeVar

from ..config import BaseCsvConfig
from .base_bean import BaseBean


C = TypeVar("C", bound=BaseCsvConfig)


class BaseCsvEntity(BaseBean[C], ABC):
    @classmethod
    def _get_csv_filepath(cls) -> str:
        return cls._get_config_class()._get_csv_filepath()
