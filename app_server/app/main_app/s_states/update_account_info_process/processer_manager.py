from typing import Dict, Any, Tuple, Type

from ..signed_in_account_entity import SignedInAccountEntity
from ...forms import UpdateAccountInfoForm
from ....base import BaseProcessersManager, EarlyStopProcessException
from model import BaseResponse


class UpdateAccountInfoProcesserResponse(BaseResponse[None]):
    pass


class UpdateAccountInfoProcesserManager(BaseProcessersManager[UpdateAccountInfoProcesserResponse]):
    def _pre_process_for_starting(self, **kwargs) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]

        try:
            inner_dict = {}
            inner_dict["form"] = UpdateAccountInfoForm.init_from_dict(kwargs=kwargs)
        except:
            raise EarlyStopProcessException(message="Please input form corectly.")
        return outer_dict, inner_dict

    def _pre_process_for_running(self, **kwargs) -> Dict[str, Any]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]

        kwargs["message_area"].warning("Running.")
        return outer_dict

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> UpdateAccountInfoProcesserResponse:
        response = inner_dict["response"]
        if response.is_success:
            SignedInAccountEntity.set(value=response.contents)
        return UpdateAccountInfoProcesserResponse(is_success=response.is_success, message=response.message)

    @staticmethod
    def _get_response_class() -> Type[UpdateAccountInfoProcesserResponse]:
        return UpdateAccountInfoProcesserResponse
