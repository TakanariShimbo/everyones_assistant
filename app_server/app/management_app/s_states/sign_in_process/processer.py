from typing import Dict, Any

from ....base import BaseProcesser
from .form import Form
from controller import AccountManager


class Processer(BaseProcesser[None]):
    def _main_process(self, inner_dict: Dict[str, Any]) -> None:
        form: Form = inner_dict["form"]
        inner_dict["response"] = AccountManager.sign_in(
            account_id=form.account_id,
            raw_password=form.raw_password,
            to_management_page=True,
        )

    def _pre_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _callback_process(self, content: None, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass
