from typing import Any, Type, Union
from datetime import datetime

from ..handler import DateHandler
from ..base import BaseDto
from ..configs import ChatRoomDtoConfig


class ChatRoomDto(BaseDto[ChatRoomDtoConfig]):
    def __init__(
        self,
        room_id: str,
        room_title: str,
        room_created_at: Union[str, datetime],
        room_is_disabled: bool,
        account_id: str,
        account_mail_address: str,
        account_family_name_en: str,
        account_given_name_en: str,
        account_family_name_jp: str,
        account_given_name_jp: str,
        account_hashed_password: str,
        account_registered_at: Union[str, datetime],
        account_is_disabled: bool,
        release_id: str,
        release_label_en: str,
        release_label_jp: str,
    ) -> None:
        self._room_id = room_id
        self._room_title = room_title
        self._room_created_at = DateHandler.to_str(date=room_created_at)
        self._room_is_disabled = room_is_disabled

        self._account_id = account_id
        self._account_mail_address = account_mail_address
        self._account_family_name_en = account_family_name_en
        self._account_given_name_en = account_given_name_en
        self._account_family_name_jp = account_family_name_jp
        self._account_given_name_jp = account_given_name_jp
        self._account_hashed_password = account_hashed_password
        self._account_registered_at = DateHandler.to_str(date=account_registered_at)
        self._account_is_disabled = account_is_disabled

        self._release_id = release_id
        self._release_label_en = release_label_en
        self._release_label_jp = release_label_jp


    @property
    def room_id(self) -> str:
        return self._room_id

    @property
    def room_title(self) -> str:
        return self._room_title

    @property
    def room_created_at(self) -> str:
        return self._room_created_at

    @property
    def room_is_disabled(self) -> bool:
        return self._room_is_disabled

    @property
    def room_created_at_short(self) -> str:
        return self.room_created_at.split(sep=" ")[0]


    @property
    def account_id(self) -> str:
        return self._account_id

    @property
    def account_mail_address(self) -> str:
        return self._account_mail_address

    @property
    def account_family_name_en(self) -> str:
        return self._account_family_name_en

    @property
    def account_given_name_en(self) -> str:
        return self._account_given_name_en

    @property
    def account_family_name_jp(self) -> str:
        return self._account_family_name_jp

    @property
    def account_given_name_jp(self) -> str:
        return self._account_given_name_jp

    @property
    def account_hashed_password(self) -> str:
        return self._account_hashed_password

    @property
    def account_registered_at(self) -> str:
        return self._account_registered_at

    @property
    def account_is_disabled(self) -> bool:
        return self._account_is_disabled

    @property
    def account_registered_at_short(self) -> str:
        return self.account_registered_at.split(sep=" ")[0]


    @property
    def release_id(self) -> str:
        return self._release_id

    @property
    def release_label_en(self) -> str:
        return self._release_label_en

    @property
    def release_label_jp(self) -> str:
        return self._release_label_jp


    def _check_is_same(self, other: Any) -> bool:
        return False

    @staticmethod
    def _get_config_class() -> Type[ChatRoomDtoConfig]:
        return ChatRoomDtoConfig
