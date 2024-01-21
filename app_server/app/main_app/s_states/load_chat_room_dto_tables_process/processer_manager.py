from typing import Dict, Any, Tuple, Type

from ....base import BaseProcesserManager
from ..signed_in_account_entity import SignedInAccountEntity
from ..loaded_yours_chat_room_dto_table import LoadedYoursChatRoomDtoTable
from ..loaded_everyone_chat_room_dto_table import LoadedEveryoneChatRoomDtoTable
from model import BaseResponse


class ProcesserResponse(BaseResponse[None]):
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
        LoadedYoursChatRoomDtoTable.set(value=inner_dict["yours_table"])
        LoadedEveryoneChatRoomDtoTable.set(value=inner_dict["everyone_table"])
        return ProcesserResponse(is_success=True)

    @staticmethod
    def _get_response_class() -> Type[ProcesserResponse]:
        return ProcesserResponse
