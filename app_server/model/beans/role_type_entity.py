from typing import Any, Type

from ..base import BaseBean
from ..configs import RoleTypeConfig


class RoleTypeEntity(BaseBean[RoleTypeConfig]):
    def __init__(self, role_id: str, label_en: str, label_jp: str):
        self._role_id = role_id
        self._label_en = label_en
        self._label_jp = label_jp

    @property
    def role_id(self) -> str:
        return self._role_id

    @property
    def label_en(self) -> str:
        return self._label_en

    @property
    def label_jp(self) -> str:
        return self._label_jp

    def _check_is_same(self, other: Any) -> bool:
        if not isinstance(other, RoleTypeEntity):
            return False
        return self.role_id == other.role_id

    @staticmethod
    def _get_config_class() -> Type[RoleTypeConfig]:
        return RoleTypeConfig
