from typing import List

import pandas as pd

from ..base import ColumnConfig, BaseDtoConfig


class ChatRoomDtoConfig(BaseDtoConfig):
    @staticmethod
    def _get_column_configs() -> List[ColumnConfig]:
        return [
            ColumnConfig(name="room_id", dtype=pd.StringDtype()),
            ColumnConfig(name="room_title", dtype=pd.StringDtype()),
            ColumnConfig(name="room_created_at", dtype=pd.StringDtype()),

            ColumnConfig(name="account_id", dtype=pd.StringDtype()),
            ColumnConfig(name="account_mail_address", dtype=pd.StringDtype()),
            ColumnConfig(name="account_family_name_en", dtype=pd.StringDtype()),
            ColumnConfig(name="account_given_name_en", dtype=pd.StringDtype()),
            ColumnConfig(name="account_family_name_jp", dtype=pd.StringDtype()),
            ColumnConfig(name="account_given_name_jp", dtype=pd.StringDtype()),
            ColumnConfig(name="account_hashed_password", dtype=pd.StringDtype()),
            ColumnConfig(name="account_registered_at", dtype=pd.StringDtype()),

            ColumnConfig(name="release_id", dtype=pd.StringDtype()),
            ColumnConfig(name="release_label_en", dtype=pd.StringDtype()),
            ColumnConfig(name="release_label_jp", dtype=pd.StringDtype()),
        ]

