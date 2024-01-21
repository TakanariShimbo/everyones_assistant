from typing import Dict, Any, Tuple, Type

from ....base import BaseProcessersManager, EarlyStopProcessException
from ..signed_in_account_entity import SignedInAccountEntity
from ..entered_room_manager import EnteredRoomManager
from .form import Form
from model import BaseResponse


class QueryProcesserResponse(BaseResponse[None]):
    pass


class ProcesserManager(BaseProcessersManager[QueryProcesserResponse]):
    def _pre_process_for_starting(self, **kwargs) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]
        outer_dict["history_area"] = kwargs["history_area"]

        try:
            inner_dict = {}
            inner_dict["form"] = Form.from_entity(assistant_entity=kwargs["assistant_entity"], prompt=kwargs["prompt"])
            inner_dict["manager"] = EnteredRoomManager.get()
            inner_dict["account"] = SignedInAccountEntity.get()
        except:
            raise EarlyStopProcessException(message="Please input form corectly.")
        return outer_dict, inner_dict

    def _pre_process_for_running(self, **kwargs) -> Dict[str, Any]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]
        outer_dict["history_area"] = kwargs["history_area"]

        kwargs["message_area"].warning("Running.")
        return outer_dict

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> QueryProcesserResponse:
        return QueryProcesserResponse(is_success=True)

    @staticmethod
    def _get_response_class() -> Type[QueryProcesserResponse]:
        return QueryProcesserResponse
