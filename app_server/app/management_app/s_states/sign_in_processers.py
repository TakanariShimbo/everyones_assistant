from typing import Dict, Any, Tuple, Type

from ..forms import SignInForm
from ...base import BaseProcesser, BaseProcessersManager, EarlyStopProcessException
from controller import AccountManager
from model import BaseResponse


class SignInProcesser(BaseProcesser[None]):
    def _main_process(self, inner_dict: Dict[str, Any]) -> None:
        sign_in_form: SignInForm = inner_dict["form"]
        inner_dict["response"] = AccountManager.sign_in(
            account_id=sign_in_form.account_id,
            raw_password=sign_in_form.raw_password,
            to_management=True,
        )

    def _pre_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _callback_process(self, content: None, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass


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
