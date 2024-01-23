from typing import Dict, Any

from ....base import BaseProcesser
from controller import ChatRoomManager


class Processer(BaseProcesser[None]):
    def _main_process(self, inner_dict: Dict[str, Any]) -> None:
        inner_dict["manager"] = ChatRoomManager.init_as_continue(
            room_id=inner_dict["room_id"],
            signed_in_account_id=inner_dict["signed_in_account_id"],
        )

    def _pre_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _callback_process(self, content: None, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass
