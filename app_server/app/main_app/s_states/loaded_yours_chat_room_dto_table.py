from ...base import BaseSStateNoDefault
from model import ChatRoomDtoTable


class LoadedYoursChatRoomDtoTable(BaseSStateNoDefault[ChatRoomDtoTable]):
    @staticmethod
    def get_name() -> str:
        return "LOADED_YOURS_CHAT_ROOM_DTO_TABLE"
