from typing import Type

from sqlalchemy import Engine

from ..base import BaseTable
from ..configs import ChatMessageConfig, ChatRoomConfig
from ..beans import ChatMessageEntity


class ChatMessageTable(BaseTable[ChatMessageConfig, ChatMessageEntity]):
    @staticmethod
    def _get_config_class() -> Type[ChatMessageConfig]:
        return ChatMessageConfig

    @staticmethod
    def _get_bean_class() -> Type[ChatMessageEntity]:
        return ChatMessageEntity

    @classmethod
    def load_specified_room_from_database(cls, database_engine: Engine, room_id: str) -> "ChatMessageTable":
        statement, parameters = cls._get_simple_select_sql(
            column_name=ChatRoomConfig.get_key_column_name(),
            value=room_id,
        )
        return cls.load_from_database(database_engine=database_engine, statement=statement, parameters=parameters)
