from typing import Any, Type

from ..base import BaseCsvEntity
from ..configs import ProviderTypeConfig


class ProviderTypeEntity(BaseCsvEntity[ProviderTypeConfig]):
    def __init__(self, provider_id: str, label_en: str, label_jp: str):
        self._provider_id = provider_id
        self._label_en = label_en
        self._label_jp = label_jp

    @property
    def provider_id(self) -> str:
        return self._provider_id

    @property
    def label_en(self) -> str:
        return self._label_en

    @property
    def label_jp(self) -> str:
        return self._label_jp

    def _check_is_same(self, other: Any) -> bool:
        if not isinstance(other, ProviderTypeEntity):
            return False
        return self.provider_id == other.provider_id

    @staticmethod
    def _get_config_class() -> Type[ProviderTypeConfig]:
        return ProviderTypeConfig
