from typing import Dict, Any, Tuple, Type

from ....base import BaseProcessersManager
from controller import ChatRoomManager
from model import BaseResponse


class ProcesserResponse(BaseResponse[ChatRoomManager]):
    pass


class ProcesserManager(BaseProcessersManager[ProcesserResponse]):
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

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> ProcesserResponse:
        return ProcesserResponse(is_success=True, contents=inner_dict["manager"])

    @staticmethod
    def _get_response_class() -> Type[ProcesserResponse]:
        return ProcesserResponse
