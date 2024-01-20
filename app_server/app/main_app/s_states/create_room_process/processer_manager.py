from typing import Dict, Any, Tuple, Type

from ....base import BaseProcessersManager, EarlyStopProcessException
from ...forms import CreateForm
from ..signed_in_account_entity import SignedInAccountEntity
from controller import ChatRoomManager
from model import BaseResponse


class ProcesserResponse(BaseResponse[ChatRoomManager]):
    pass


class ProcesserManager(BaseProcessersManager[ProcesserResponse]):
    def _pre_process_for_starting(self, **kwargs) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]

        inner_dict = {}
        try:
            inner_dict["form"] = CreateForm.from_entity(
                account_entity=SignedInAccountEntity.get(),
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
        return ProcesserResponse(is_success=True, contents=inner_dict["manager"])

    @staticmethod
    def _get_response_class() -> Type[ProcesserResponse]:
        return ProcesserResponse