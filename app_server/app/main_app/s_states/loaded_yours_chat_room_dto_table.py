from ...base import BaseSStateHasDefault
from model import ChatRoomDtoTable


class LoadedYoursChatRoomDtoTable(BaseSStateHasDefault[ChatRoomDtoTable]):
    @staticmethod
    def get_name() -> str:
        return "LOADED_YOURS_CHAT_ROOM_DTO_TABLE"
