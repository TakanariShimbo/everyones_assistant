from typing import Dict, Any

from ....base import BaseProcesser
from .form import Form
from controller import AccountManager


class Processer(BaseProcesser[None]):
    def _main_process(self, inner_dict: Dict[str, Any]) -> None:
        form: Form = inner_dict["form"]
        inner_dict["response"] = AccountManager.sign_up(
            account_id=form.account_id,
            mail_address=form.mail_address,
            family_name_en=form.family_name_en,
            given_name_en=form.given_name_en,
            family_name_jp=form.family_name_jp,
            given_name_jp=form.given_name_jp,
            raw_password=form.raw_password,
            is_user=form.is_user,
            is_administrator=form.is_administrator,
        )

    def _pre_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _callback_process(self, content: None, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass
