from typing import Dict, Any, Tuple

from ..main_forms import CreateForm
from .main_component_s_states import MainComponentSState
from .account_s_states import AccountSState
from .chat_room_s_states import ChatRoomSState
from ...base import BaseProcesser, BaseProcessersManager, EarlyStopProcessException
from controller import ChatRoomManager


class CreateProcesser(BaseProcesser[None]):
    def main_process(self, inner_dict: Dict[str, Any]) -> None:
        form: CreateForm = inner_dict["form"]
        inner_dict["chat_message_manager"] = ChatRoomManager.init_as_new(
            account_id=form.account_id,
            title=form.title,
            release_id=form.release_id,
        )

    def pre_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def callback_process(self, content: None, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass


class CreateProcesserManager(BaseProcessersManager):
    def pre_process_for_starting(self, **kwargs) -> Tuple[Dict[str, Any], Dict[str, Any]]:
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
            outer_dict["message_area"].warning("Please input form corectly.")
            raise EarlyStopProcessException()
        return outer_dict, inner_dict

    def pre_process_for_running(self, **kwargs) -> Dict[str, Any]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]

        kwargs["message_area"].warning("Running.")
        return outer_dict

    def post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> bool:
        outer_dict["message_area"].empty()
        ChatRoomSState.set(value=inner_dict["chat_message_manager"])
        MainComponentSState.set_chat_room_entity()
        return True