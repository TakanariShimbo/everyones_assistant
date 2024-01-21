from typing import Dict, Any, Tuple, Type

from ....base import BaseProcesserManager, EarlyStopProcessException
from ..signed_in_account_entity import SignedInAccountEntity
from .form import Form
from model import BaseResponse


class ProcesserResponse(BaseResponse[None]):
    pass


class ProcesserManager(BaseProcesserManager[ProcesserResponse]):
    def _pre_process_for_starting(self, **kwargs) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]

        try:
            inner_dict = {}
            inner_dict["form"] = Form.init(
                account_id=SignedInAccountEntity.get().account_id,
                kwargs=kwargs,
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
        response = inner_dict["response"]
        if response.is_success:
            SignedInAccountEntity.set(value=response.contents)
        return ProcesserResponse(is_success=response.is_success, message=response.message)

    @staticmethod
    def _get_response_class() -> Type[ProcesserResponse]:
        return ProcesserResponse
