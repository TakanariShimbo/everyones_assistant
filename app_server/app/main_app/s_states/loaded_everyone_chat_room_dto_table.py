from ...base import BaseSState
from model import ChatRoomDtoTable


class LoadedEveryoneChatRoomDtoTable(BaseSState[ChatRoomDtoTable]):
    @staticmethod
    def get_name() -> str:
        return "LOADED_EVERYONE_CHAT_ROOM_DTO_TABLE"
