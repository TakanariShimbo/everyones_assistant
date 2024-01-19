from typing import Dict, Any, Tuple, Type

from .account_s_states import AccountSState
from ..forms import ChangeAccountPassForm
from ...base import BaseProcesser, BaseProcessersManager, EarlyStopProcessException
from controller import AccountManager
from model import BaseResponse


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


class ChangeAccountPassProcesserResponse(BaseResponse[None]):
    pass


class ChangeAccountPassProcesserManager(BaseProcessersManager[ChangeAccountPassProcesserResponse]):
    def _pre_process_for_starting(self, **kwargs) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]

        try:
            inner_dict = {}
            inner_dict["form"] = ChangeAccountPassForm.init_from_dict(kwargs=kwargs)
        except:
            raise EarlyStopProcessException(message="Please input form corectly.")
        return outer_dict, inner_dict

    def _pre_process_for_running(self, **kwargs) -> Dict[str, Any]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]

        kwargs["message_area"].warning("Running.")
        return outer_dict

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> ChangeAccountPassProcesserResponse:
        response = inner_dict["response"]
        if response.is_success:
            AccountSState.set(value=response.contents)
        return ChangeAccountPassProcesserResponse(is_success=response.is_success, message=response.message)

    @staticmethod
    def _get_response_class() -> Type[ChangeAccountPassProcesserResponse]:
        return ChangeAccountPassProcesserResponse
