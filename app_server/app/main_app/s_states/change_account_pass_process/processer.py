from typing import Dict, Any

from ...forms import ChangeAccountPassForm
from ....base import BaseProcesser
from controller import AccountManager


class ChangeAccountPassProcesser(BaseProcesser[None]):
    def _main_process(self, inner_dict: Dict[str, Any]) -> None:
        form: ChangeAccountPassForm = inner_dict["form"]
        inner_dict["response"] = AccountManager.change_password(
            account_id=form.account_id,
            current_raw_password=form.current_raw_password,
            new_raw_password=form.new_raw_password,
        )

    def _pre_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _callback_process(self, content: None, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass
