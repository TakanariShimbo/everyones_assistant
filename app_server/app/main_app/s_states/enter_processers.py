from typing import Dict, Any, Tuple, Type

from ...base import BaseProcesser, BaseProcessersManager
from controller import ChatRoomManager
from model import BaseResponse


class EnterProcesser(BaseProcesser[None]):
    def _main_process(self, inner_dict: Dict[str, Any]) -> None:
        inner_dict["chat_message_manager"] = ChatRoomManager.init_as_continue(
            room_id=inner_dict["room_id"],
            account_id=inner_dict["account_id"],
            release_id=inner_dict["release_id"],
        )

    def _pre_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _callback_process(self, content: None, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass


class EnterProcesserResponse(BaseResponse[ChatRoomManager]):
    pass


class EnterProcesserManager(BaseProcessersManager[EnterProcesserResponse]):
    def _pre_process_for_starting(self, **kwargs) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        outer_dict = {}
        inner_dict = {}
        inner_dict["room_id"] = kwargs["room_id"]
        inner_dict["account_id"] = kwargs["account_id"]
        inner_dict["release_id"] = kwargs["release_id"]
        return outer_dict, inner_dict

    def _pre_process_for_running(self, **kwargs) -> Dict[str, Any]:
        outer_dict = {}
        return outer_dict

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> EnterProcesserResponse:
        return EnterProcesserResponse(is_success=True, contents=inner_dict["chat_message_manager"])

    @staticmethod
    def _get_response_class() -> Type[EnterProcesserResponse]:
        return EnterProcesserResponse