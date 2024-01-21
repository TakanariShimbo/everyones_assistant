from typing import Dict, Any

from ....base import BaseProcesser
from model import Database, ChatRoomDtoTable


class Processer(BaseProcesser[None]):
    def _main_process(self, inner_dict: Dict[str, Any]) -> None:
        account_id = inner_dict["account_id"]
        yours_chat_room_table = ChatRoomDtoTable.load_not_disabled_and_specified_account_from_database(
            database_engine=Database.ENGINE,
            account_id=account_id,
        )
        everyone_chat_room_table = ChatRoomDtoTable.load_public_and_not_disabled_and_unspecified_account_from_database(
            database_engine=Database.ENGINE,
            account_id=account_id,
        )
        inner_dict["yours_table"] = yours_chat_room_table
        inner_dict["everyone_table"] = everyone_chat_room_table

    def _pre_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _callback_process(self, content: None, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass
