from typing import Dict, Any

from ...forms import CreateForm
from ....base import BaseProcesser
from controller import ChatRoomManager


class CreateRoomProcesser(BaseProcesser[None]):
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


