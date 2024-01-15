from typing import List

import pandas as pd

from ..base import ColumnConfig, BaseColumnConfigEnum, BaseDtoConfig


class ChatRoomDtoColumnConfigs(BaseColumnConfigEnum):
    ROOM_ID = ColumnConfig(name="room_id", dtype=pd.StringDtype())
    ROOM_TITLE = ColumnConfig(name="room_title", dtype=pd.StringDtype())
    ROOM_CREATED_AT = ColumnConfig(name="room_created_at", dtype=pd.StringDtype())

    ACCOUNT_ID = ColumnConfig(name="account_id", dtype=pd.StringDtype())
    ACCOUNT_MAIL_ADDRESS = ColumnConfig(name="account_mail_address", dtype=pd.StringDtype())
    ACCOUNT_FAMILY_NAME_EN = ColumnConfig(name="account_family_name_en", dtype=pd.StringDtype())
    ACCOUNT_GIVEN_NAME_EN = ColumnConfig(name="account_given_name_en", dtype=pd.StringDtype())
    ACCOUNT_FAMILY_NAME_JP = ColumnConfig(name="account_family_name_jp", dtype=pd.StringDtype())
    ACCOUNT_GIVEN_NAME_JP = ColumnConfig(name="account_given_name_jp", dtype=pd.StringDtype())
    ACCOUNT_HASHED_PASSWORD = ColumnConfig(name="account_hashed_password", dtype=pd.StringDtype())
    ACCOUNT_REGISTERED_AT = ColumnConfig(name="account_registered_at", dtype=pd.StringDtype())

    RELEASE_ID = ColumnConfig(name="release_id", dtype=pd.StringDtype())
    RELEASE_LABEL_EN = ColumnConfig(name="release_label_en", dtype=pd.StringDtype())
    RELEASE_LABEL_JP = ColumnConfig(name="release_label_jp", dtype=pd.StringDtype())


class ChatRoomDtoConfig(BaseDtoConfig):
    @staticmethod
    def _get_column_configs() -> List[ColumnConfig]:
        return ChatRoomDtoColumnConfigs.to_list()
