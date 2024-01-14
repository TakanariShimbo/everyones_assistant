from typing import Any, Type

from ..base import BaseCsvEntity
from ..configs import AssistantTypeConfig


class AssistantTypeEntity(BaseCsvEntity[AssistantTypeConfig]):
    def __init__(self, assistant_id: str, provider_id: str, ai_model_id: str, label_en: str, label_jp: str):
        self._assistant_id = assistant_id
        self._provider_id = provider_id
        self._ai_model_id = ai_model_id
        self._label_en = label_en
        self._label_jp = label_jp

    @property
    def assistant_id(self) -> str:
        return self._assistant_id

    @property
    def provider_id(self) -> str:
        return self._provider_id

    @property
    def ai_model_id(self) -> str:
        return self._ai_model_id

    @property
    def label_en(self) -> str:
        return self._label_en

    @property
    def label_jp(self) -> str:
        return self._label_jp

    def _check_is_same(self, other: Any) -> bool:
        if not isinstance(other, AssistantTypeEntity):
            return False
        return self.assistant_id == other.assistant_id

    @staticmethod
    def _get_config_class() -> Type[AssistantTypeConfig]:
        return AssistantTypeConfig