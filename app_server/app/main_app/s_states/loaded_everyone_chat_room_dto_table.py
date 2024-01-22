from ...base import BaseSStateNoDefault
from model import ChatRoomDtoTable


class LoadedEveryoneChatRoomDtoTable(BaseSStateNoDefault[ChatRoomDtoTable]):
    @staticmethod
    def get_name() -> str:
        return "LOADED_EVERYONE_CHAT_ROOM_DTO_TABLE"
