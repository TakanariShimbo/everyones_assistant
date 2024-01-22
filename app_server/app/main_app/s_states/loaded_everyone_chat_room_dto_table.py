from ...base import BaseSStateHasDefault
from model import ChatRoomDtoTable


class LoadedEveryoneChatRoomDtoTable(BaseSStateHasDefault[ChatRoomDtoTable]):
    @staticmethod
    def get_name() -> str:
        return "LOADED_EVERYONE_CHAT_ROOM_DTO_TABLE"
