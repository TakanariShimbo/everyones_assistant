from typing import Dict, Any, Tuple

from .account_s_states import AccountSState
from ..main_forms import UpdateAccountInfoForm
from ..base import BaseProcesser, BaseProcessersManager, EarlyStopProcessException
from controller import AccountManager


class UpdateAccountInfoProcesser(BaseProcesser[None]):
    def main_process(self, inner_dict: Dict[str, Any]) -> None:
        form: UpdateAccountInfoForm = inner_dict["form"]
        inner_dict["response"] = AccountManager.update_info(
            account_id=form.account_id,
            mail_address=form.mail_address,
            family_name_en=form.family_name_en,
            given_name_en=form.given_name_en,
            family_name_jp=form.family_name_jp,
            given_name_jp=form.given_name_jp,
            raw_password=form.raw_password,
        )

    def pre_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def callback_process(self, content: None, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass


class UpdateAccountInfoProcesserManager(BaseProcessersManager):
    def pre_process_for_starting(self, **kwargs) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]

        try:
            inner_dict = {}
            inner_dict["form"] = UpdateAccountInfoForm.init_from_dict(kwargs=kwargs)
        except:
            outer_dict["message_area"].warning("Please input form corectly.")
            raise EarlyStopProcessException()
        return outer_dict, inner_dict

    def pre_process_for_running(self, **kwargs) -> Dict[str, Any]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]

        kwargs["message_area"].warning("Running.")
        return outer_dict

    def post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> bool:
        if not inner_dict["response"].is_success:
            outer_dict["message_area"].warning(inner_dict["response"].message)
            return False

        AccountSState.set(value=inner_dict["response"].contents)
        outer_dict["message_area"].success(inner_dict["response"].message)
        return True
