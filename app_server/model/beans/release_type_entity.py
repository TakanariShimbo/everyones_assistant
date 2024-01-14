from typing import Any, Type

from ..base import BaseCsvEntity
from ..configs import ReleaseTypeConfig


class ReleaseTypeEntity(BaseCsvEntity[ReleaseTypeConfig]):
    def __init__(self, release_id: str, label_en: str, label_jp: str):
        self._release_id = release_id
        self._label_en = label_en
        self._label_jp = label_jp

    @property
    def release_id(self) -> str:
        return self._release_id

    @property
    def label_en(self) -> str:
        return self._label_en

    @property
    def label_jp(self) -> str:
        return self._label_jp

    def _check_is_same(self, other: Any) -> bool:
        if not isinstance(other, ReleaseTypeEntity):
            return False
        return self.release_id == other.release_id

    @staticmethod
    def _get_config_class() -> Type[ReleaseTypeConfig]:
        return ReleaseTypeConfig
