from typing import Dict, Any, Tuple, Type

from ..forms import SignUpForm
from ...base import BaseProcesser, BaseProcessersManager, EarlyStopProcessException
from controller import AccountManager
from model import BaseResponse


class SignUpProcesser(BaseProcesser[None]):
    def _main_process(self, inner_dict: Dict[str, Any]) -> None:
        form: SignUpForm = inner_dict["form"]
        inner_dict["response"] = AccountManager.sign_up(
            account_id=form.account_id,
            mail_address=form.mail_address,
            family_name_en=form.family_name_en,
            given_name_en=form.given_name_en,
            family_name_jp=form.family_name_jp,
            given_name_jp=form.given_name_jp,
            raw_password=form.raw_password,
        )

    def _pre_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _callback_process(self, content: None, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass


class SignUpProcesserResponse(BaseResponse[None]):
    pass


class SignUpProcesserManager(BaseProcessersManager[SignUpProcesserResponse]):
    def _pre_process_for_starting(self, **kwargs) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]

        try:
            inner_dict = {}
            inner_dict["form"] = SignUpForm.init_from_dict_after_compare_passwords(kwargs=kwargs)
        except:
            raise EarlyStopProcessException(message="Please input form corectly.")
        return outer_dict, inner_dict

    def _pre_process_for_running(self, **kwargs) -> Dict[str, Any]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]

        kwargs["message_area"].warning("Running.")
        return outer_dict

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> SignUpProcesserResponse:
        response = inner_dict["response"]
        return SignUpProcesserResponse(is_success=response.is_success, message=response.message)

    @staticmethod
    def _get_response_class() -> Type[SignUpProcesserResponse]:
        return SignUpProcesserResponse
