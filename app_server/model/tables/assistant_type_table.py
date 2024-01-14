from typing import Type

from ..base import BaseCsvTable
from ..configs import AssistantTypeConfig
from ..beans import AssistantTypeEntity


class AssistantTypeTable(BaseCsvTable[AssistantTypeConfig, AssistantTypeEntity]):
    @staticmethod
    def _get_config_class() -> Type[AssistantTypeConfig]:
        return AssistantTypeConfig
    
    @staticmethod
    def _get_bean_class() -> Type[AssistantTypeEntity]:
        return AssistantTypeEntity


ASSISTANT_TYPE_TABLE = AssistantTypeTable.load_from_csv()
