from typing import Dict, Any, Tuple, Type

from ....base import BaseProcesserManager
from ..signed_in_account_entity import SignedInAccountEntity
from model import BaseResponse, ChatRoomDtoTable


class ChatRoomDtoTables:
    def __init__(self, yours_chat_room_table: ChatRoomDtoTable, everyone_chat_room_table: ChatRoomDtoTable):
        self._yours_chat_room_table = yours_chat_room_table
        self._everyone_chat_room_table = everyone_chat_room_table

    @property
    def yours_chat_room_table(self) -> ChatRoomDtoTable:
        return self._yours_chat_room_table

    @property
    def everyone_chat_room_table(self) -> ChatRoomDtoTable:
        return self._everyone_chat_room_table


class ProcesserResponse(BaseResponse[ChatRoomDtoTables]):
    pass


class ProcesserManager(BaseProcesserManager[ProcesserResponse]):
    def _pre_process_for_starting(self, **kwargs) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        outer_dict = {}
        inner_dict = {}
        inner_dict["account_id"] = SignedInAccountEntity.get().account_id
        return outer_dict, inner_dict

    def _pre_process_for_running(self, **kwargs) -> Dict[str, Any]:
        outer_dict = {}
        return outer_dict

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> ProcesserResponse:
        return ProcesserResponse(
            is_success=True,
            contents=ChatRoomDtoTables(
                yours_chat_room_table=inner_dict["yours_table"],
                everyone_chat_room_table=inner_dict["everyone_table"],
            ),
        )

    @staticmethod
    def _get_response_class() -> Type[ProcesserResponse]:
        return ProcesserResponse
