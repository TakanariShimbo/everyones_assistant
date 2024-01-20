from typing import Dict, Any

from ....base import BaseProcesser
from controller import ChatRoomManager


class EnterRoomProcesser(BaseProcesser[None]):
    def _main_process(self, inner_dict: Dict[str, Any]) -> None:
        inner_dict["chat_message_manager"] = ChatRoomManager.init_as_continue(
            room_id=inner_dict["room_id"],
            account_id=inner_dict["account_id"],
            release_id=inner_dict["release_id"],
        )

    def _pre_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _callback_process(self, content: None, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass
