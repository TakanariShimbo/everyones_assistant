from typing import Any, Optional, Type, Union
from datetime import datetime

from sqlalchemy import Engine

from ..handler import DateHandler, HashHandler
from ..base import BaseDatabaseEntity
from ..configs import AccountConfig, AccountColumnConfigs


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
    ) -> None:
        self._account_id = account_id
        self._mail_address = mail_address
        self._family_name_en = family_name_en
        self._given_name_en = given_name_en
        self._family_name_jp = family_name_jp
        self._given_name_jp = given_name_jp
        self._hashed_password = hashed_password
        self._registered_at = DateHandler.to_str_or_none(date=registered_at)

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
        registered_at: Optional[Union[str, datetime]] = None
    ) -> "AccountEntity":
        
        hashed_password = HashHandler.hash(raw_contents=raw_password)
        
        return cls(
            account_id=account_id,
            mail_address=mail_address,
            family_name_en=family_name_en,
            given_name_en=given_name_en,
            family_name_jp=family_name_jp,
            given_name_jp=given_name_jp,
            hashed_password=hashed_password,
            registered_at=registered_at
        )

    @property
    def account_id(self) -> str:
        return self._account_id

    @property
    def mail_address(self) -> str:
        return self._mail_address

    @property
    def family_name_en(self) -> str:
        return self._family_name_en

    @property
    def given_name_en(self) -> str:
        return self._given_name_en

    @property
    def family_name_jp(self) -> str:
        return self._family_name_jp

    @property
    def given_name_jp(self) -> str:
        return self._given_name_jp

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
    def registered_at_short(self) -> str:
        return self.registered_at.split(sep=" ")[0]

    def _check_is_same(self, other: Any) -> bool:
        return False

    @staticmethod
    def _get_config_class() -> Type[AccountConfig]:
        return AccountConfig

    @classmethod
    def load_specified_id_from_database(cls, database_engine: Engine, account_id: str) -> "AccountEntity":
        return cls.load_from_database(database_engine=database_engine, column_name=AccountColumnConfigs.get_key_column_name(), value=account_id)

    def verify_password(self, raw_password: str) -> bool:
        return HashHandler.verify(raw_contents=raw_password, hashed_contents=self.hashed_password)