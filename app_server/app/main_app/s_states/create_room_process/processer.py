from typing import Dict, Any

from ....base import BaseProcesser
from ...forms import CreateForm
from controller import ChatRoomManager


class Processer(BaseProcesser[None]):
    def _main_process(self, inner_dict: Dict[str, Any]) -> None:
        form: CreateForm = inner_dict["form"]
        inner_dict["manager"] = ChatRoomManager.init_as_new(
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


