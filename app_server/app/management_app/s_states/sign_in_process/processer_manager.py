from typing import Dict, Any, Tuple, Type

from ...forms import SignInForm
from ....base import BaseProcessersManager, EarlyStopProcessException
from model import BaseResponse


class SignInProcesserResponse(BaseResponse[None]):
    pass


class SignInProcesserManager(BaseProcessersManager[SignInProcesserResponse]):
    def _pre_process_for_starting(self, **kwargs) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]

        try:
            inner_dict = {}
            inner_dict["form"] = SignInForm.init(kwargs=kwargs)
        except:
            raise EarlyStopProcessException(message="Please input form corectly.")
        return outer_dict, inner_dict

    def _pre_process_for_running(self, **kwargs) -> Dict[str, Any]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]

        kwargs["message_area"].warning("Running.")
        return outer_dict

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> SignInProcesserResponse:
        response = inner_dict["response"]
        return SignInProcesserResponse(is_success=response.is_success, message=response.message)

    @staticmethod
    def _get_response_class() -> Type[SignInProcesserResponse]:
        return SignInProcesserResponse