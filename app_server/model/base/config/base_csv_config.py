from abc import ABC, abstractmethod

from .base_config import BaseConfig


class BaseCsvConfig(BaseConfig, ABC):
    @staticmethod
    @abstractmethod
    def _get_csv_filepath() -> str:
        raise NotImplementedError("Subclasses must implement this method")
