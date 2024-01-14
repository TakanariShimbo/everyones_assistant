from typing import List
from textwrap import dedent

import pandas as pd

from ..base import ColumnConfig, BaseConfig


class ChatRoomConfig(BaseConfig):
    @staticmethod
    def _get_column_configs() -> List[ColumnConfig]:
        return [
            ColumnConfig(name="room_id", dtype=pd.StringDtype(), auto_assigned=False),
            ColumnConfig(name="account_id", dtype=pd.StringDtype(), auto_assigned=False),
            ColumnConfig(name="title", dtype=pd.StringDtype(), auto_assigned=False),
            ColumnConfig(name="release_id", dtype=pd.StringDtype(), auto_assigned=False),
            ColumnConfig(name="created_at", dtype=pd.StringDtype(), auto_assigned=True),
        ]

    @staticmethod
    def _get_database_table_name() -> str:
        return "chat_rooms"
    
    @staticmethod
    def _get_database_table_creation_sql(table_name: str) -> str:
        return dedent(
            f"""
            CREATE TABLE {table_name} (
                room_id VARCHAR(255) PRIMARY KEY,
                account_id VARCHAR(255) NOT NULL,
                title VARCHAR(255) NOT NULL,
                release_id VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (account_id) REFERENCES accounts (account_id) ON DELETE CASCADE
            );
            """
        )
