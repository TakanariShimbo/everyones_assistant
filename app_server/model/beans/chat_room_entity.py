from typing import Any, Optional, Type, Union
from datetime import datetime

from sqlalchemy import Engine

from ..handler import DateHandler
from ..base import BaseDatabaseEntity
from ..configs import ChatRoomConfig


class ChatRoomEntity(BaseDatabaseEntity[ChatRoomConfig]):
    def __init__(
        self,
        room_id: str,
        account_id: str,
        title: str,
        release_id: str,
        created_at: Optional[Union[str, datetime]] = None,
        is_disabled: Optional[bool] = None,
    ) -> None:
        self._room_id = room_id
        self._account_id = account_id
        self._title = title
        self._release_id = release_id
        self._created_at = DateHandler.to_str_or_none(date=created_at)
        self._is_disabled = is_disabled

    @property
    def room_id(self) -> str:
        return self._room_id

    @property
    def account_id(self) -> str:
        return self._account_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def release_id(self) -> str:
        return self._release_id

    @property
    def created_at(self) -> str:
        created_at = self._created_at
        if created_at == None:
            raise ValueError("Not accessible due to have not constracted.")
        return created_at

    @property
    def is_disabled(self) -> bool:
        disabled = self._is_disabled
        if disabled == None:
            raise ValueError("Not accessible due to have not constracted.")
        return disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled: bool) -> None:
        self._is_disabled = is_disabled

    @property
    def created_at_short(self) -> str:
        return self.created_at.split(sep=" ")[0]

    def _check_is_same(self, other: Any) -> bool:
        return False

    @staticmethod
    def _get_config_class() -> Type[ChatRoomConfig]:
        return ChatRoomConfig

    @classmethod
    def load_specified_id_from_database(cls, database_engine: Engine, room_id: str) -> "ChatRoomEntity":
        return cls.load_from_database(database_engine=database_engine, column_name=ChatRoomConfig.get_key_column_name(), value=room_id)
