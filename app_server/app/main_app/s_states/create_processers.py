from typing import Dict, Any, Tuple, Type

from ..forms import CreateForm
from .account_s_states import AccountSState
from ...base import BaseProcesser, BaseProcessersManager, EarlyStopProcessException
from controller import ChatRoomManager
from model import BaseResponse


class CreateProcesser(BaseProcesser[None]):
    def _main_process(self, inner_dict: Dict[str, Any]) -> None:
        form: CreateForm = inner_dict["form"]
        inner_dict["chat_message_manager"] = ChatRoomManager.init_as_new(
            account_id=form.account_id,
            title=form.title,
            release_id=form.release_id,
        )

    def _pre_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _callback_process(self, content: None, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass


class CreateProcesserResponse(BaseResponse[ChatRoomManager]):
    pass


class CreateProcesserManager(BaseProcessersManager[CreateProcesserResponse]):
    def _pre_process_for_starting(self, **kwargs) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]

        inner_dict = {}
        try:
            inner_dict["form"] = CreateForm.from_entity(
                account_entity=AccountSState.get(),
                title=kwargs["title"],
                release_entity=kwargs["release_entity"]
            )
        except:
            raise EarlyStopProcessException(message="Please input form corectly.")
        return outer_dict, inner_dict

    def _pre_process_for_running(self, **kwargs) -> Dict[str, Any]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]

        kwargs["message_area"].warning("Running.")
        return outer_dict

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> CreateProcesserResponse:
        return CreateProcesserResponse(is_success=True, contents=inner_dict["chat_message_manager"])

    @staticmethod
    def _get_response_class() -> Type[CreateProcesserResponse]:
        return CreateProcesserResponse