from typing import List
from textwrap import dedent

import pandas as pd

from ..base import ColumnConfig, BaseConfig


class ChatMessageConfig(BaseConfig):
    @staticmethod
    def _get_column_configs() -> List[ColumnConfig]:
        return [
            ColumnConfig(name="message_serial_id", dtype=pd.Int64Dtype(), auto_assigned=True),
            ColumnConfig(name="room_id", dtype=pd.StringDtype(), auto_assigned=False),
            ColumnConfig(name="sender_id", dtype=pd.StringDtype(), auto_assigned=False),
            ColumnConfig(name="role_id", dtype=pd.StringDtype(), auto_assigned=False),
            ColumnConfig(name="content", dtype=pd.StringDtype(), auto_assigned=False),
            ColumnConfig(name="sent_at", dtype=pd.StringDtype(), auto_assigned=True),
        ]

    @staticmethod
    def _get_database_table_name() -> str:
        return "chat_messages"
    
    @staticmethod
    def _get_database_table_creation_sql(table_name: str) -> str:
        return dedent(
            f"""
            CREATE TABLE {table_name} (
                message_serial_id SERIAL PRIMARY KEY,
                room_id VARCHAR(255) NOT NULL,
                sender_id VARCHAR(255) NOT NULL,
                role_id VARCHAR(255) NOT NULL,
                content TEXT NOT NULL,
                sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (room_id) REFERENCES chat_rooms (room_id) ON DELETE CASCADE
            );
            """
        )
