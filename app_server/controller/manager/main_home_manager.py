from typing import List

from model import Database, ChatRoomDtoTable, ChatRoomDto


class MainHomeManager:
    def __init__(self, account_id: str) -> None:
        self._yours_chat_room_dto_table = ChatRoomDtoTable.load_not_disabled_and_specified_account_from_database(
            database_engine=Database.ENGINE,
            account_id=account_id,
        )
        self._everyone_chat_room_dto_table = ChatRoomDtoTable.load_public_and_not_disabled_and_unspecified_account_from_database(
            database_engine=Database.ENGINE,
            account_id=account_id,
        )

    def get_yours_chat_room_dtos(self) -> List[ChatRoomDto]:
        return self._everyone_chat_room_dto_table.get_all_beans()

    def get_everyone_chat_room_dtos(self) -> List[ChatRoomDto]:
        return self._everyone_chat_room_dto_table.get_all_beans()