from typing import Dict, Any, Tuple, Type

from ....base import BaseProcesserManager, EarlyStopProcessException
from ..signed_in_account_entity import SignedInAccountEntity
from ..entered_chat_room_manager import EnteredChatRoomManager
from .form import Form
from model import BaseResponse


class ProcesserResponse(BaseResponse[None]):
    pass


class ProcesserManager(BaseProcesserManager[ProcesserResponse]):
    def _pre_process_for_starting(self, **kwargs) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]

        inner_dict = {}
        try:
            inner_dict["form"] = Form.init(
                account_id=SignedInAccountEntity.get().account_id,
                title=kwargs["title"],
                release_entity=kwargs["release_entity"]
            )
        except:
            raise EarlyStopProcessException(message="Please input form corectly.")
        return outer_dict, inner_dict

    def _pre_process_for_running(self, **kwargs) -> Dict[str, Any]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]

        kwargs["message_area"].warning("Running.")
        return outer_dict

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> ProcesserResponse:
        EnteredChatRoomManager.set(value=inner_dict["manager"])
        return ProcesserResponse(is_success=True)

    @staticmethod
    def _get_response_class() -> Type[ProcesserResponse]:
        return ProcesserResponse