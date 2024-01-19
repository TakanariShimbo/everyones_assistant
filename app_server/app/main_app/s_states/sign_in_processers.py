from typing import Dict, Any, Tuple

from .account_s_states import AccountSState
from .main_component_s_states import MainComponentSState
from ..forms import SignInForm
from ...base import BaseProcesser, BaseProcessersManager, EarlyStopProcessException
from controller import AccountManager


class SignInProcesser(BaseProcesser[None]):
    def _main_process(self, inner_dict: Dict[str, Any]) -> None:
        sign_in_form: SignInForm = inner_dict["form"]
        inner_dict["response"] = AccountManager.sign_in(
            account_id=sign_in_form.account_id,
            raw_password=sign_in_form.raw_password,
            to_management=False,
        )

    def _pre_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _callback_process(self, content: None, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass


class SignInProcesserManager(BaseProcessersManager):
    def _pre_process_for_starting(self, **kwargs) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]

        try:
            inner_dict = {}
            inner_dict["form"] = SignInForm.init(kwargs=kwargs)
        except:
            outer_dict["message_area"].warning("Please input form corectly.")
            raise EarlyStopProcessException()
        return outer_dict, inner_dict

    def _pre_process_for_running(self, **kwargs) -> Dict[str, Any]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]

        kwargs["message_area"].warning("Running.")
        return outer_dict

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> bool:
        if not inner_dict["response"].is_success:
            outer_dict["message_area"].warning(inner_dict["response"].message)
            return False

        AccountSState.set(value=inner_dict["response"].contents)
        MainComponentSState.set_home_entity()
        outer_dict["message_area"].empty()
        return True
