from typing import Any, Optional, Type, Union
from datetime import datetime

from sqlalchemy import Engine

from ..handler import DateHandler, HashHandler
from ..base import BaseDatabaseEntity
from ..configs import AccountConfig


class AccountEntity(BaseDatabaseEntity[AccountConfig]):
    def __init__(
        self,
        account_id: str,
        mail_address: str,
        family_name_en: str,
        given_name_en: str,
        family_name_jp: str,
        given_name_jp: str,
        hashed_password: str,
        registered_at: Optional[Union[str, datetime]] = None,
        is_administrator: Optional[bool] = None,
        is_disabled: Optional[bool] = None,
    ) -> None:
        self._account_id = account_id
        self._mail_address = mail_address
        self._family_name_en = family_name_en
        self._given_name_en = given_name_en
        self._family_name_jp = family_name_jp
        self._given_name_jp = given_name_jp
        self._hashed_password = hashed_password
        self._registered_at = DateHandler.to_str_or_none(date=registered_at)
        self._is_administrator = is_administrator
        self._is_disabled = is_disabled

    @classmethod
    def init_with_hashing_password(
        cls,
        account_id: str,
        mail_address: str,
        family_name_en: str,
        given_name_en: str,
        family_name_jp: str,
        given_name_jp: str,
        raw_password: str,
    ) -> "AccountEntity":
        return cls(
            account_id=account_id,
            mail_address=mail_address,
            family_name_en=family_name_en,
            given_name_en=given_name_en,
            family_name_jp=family_name_jp,
            given_name_jp=given_name_jp,
            hashed_password=HashHandler.hash(raw_contents=raw_password),
        )

    @property
    def account_id(self) -> str:
        return self._account_id

    @property
    def mail_address(self) -> str:
        return self._mail_address

    @mail_address.setter
    def mail_address(self, mail_address: str) -> None:
        self._mail_address = mail_address

    @property
    def family_name_en(self) -> str:
        return self._family_name_en

    @family_name_en.setter
    def family_name_en(self, family_name_en: str) -> None:
        self._family_name_en = family_name_en

    @property
    def given_name_en(self) -> str:
        return self._given_name_en

    @given_name_en.setter
    def given_name_en(self, given_name_en: str) -> None:
        self._given_name_en = given_name_en

    @property
    def family_name_jp(self) -> str:
        return self._family_name_jp

    @family_name_jp.setter
    def family_name_jp(self, family_name_jp: str) -> None:
        self._family_name_jp = family_name_jp

    @property
    def given_name_jp(self) -> str:
        return self._given_name_jp

    @given_name_jp.setter
    def given_name_jp(self, given_name_jp: str) -> None:
        self._given_name_jp = given_name_jp

    @property
    def hashed_password(self) -> str:
        return self._hashed_password

    @property
    def registered_at(self) -> str:
        registered_at = self._registered_at
        if registered_at == None:
            raise ValueError("Not accessible due to have not constracted.")
        return registered_at

    @property
    def is_administrator(self) -> bool:
        is_administrator = self._is_administrator
        if is_administrator == None:
            raise ValueError("Not accessible due to have not constracted.")
        return is_administrator

    @property
    def is_disabled(self) -> bool:
        is_disabled = self._is_disabled
        if is_disabled == None:
            raise ValueError("Not accessible due to have not constracted.")
        return is_disabled

    @property
    def registered_at_short(self) -> str:
        return self.registered_at.split(sep=" ")[0]

    def _check_is_same(self, other: Any) -> bool:
        return False

    @staticmethod
    def _get_config_class() -> Type[AccountConfig]:
        return AccountConfig

    @classmethod
    def load_specified_id_from_database(cls, database_engine: Engine, account_id: str) -> "AccountEntity":
        return cls.load_from_database(database_engine=database_engine, column_name=AccountConfig.get_key_column_name(), value=account_id)

    def verify_password(self, raw_password: str) -> bool:
        return HashHandler.verify(raw_contents=raw_password, hashed_contents=self.hashed_password)

    def set_new_password(self, raw_password: str, new_raw_password: str) -> bool:
        if not self.verify_password(raw_password=raw_password):
            return False

        self._hashed_password = HashHandler.hash(raw_contents=new_raw_password)
        return True
