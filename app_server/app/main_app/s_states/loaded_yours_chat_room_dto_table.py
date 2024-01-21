from ...base import BaseSState
from model import ChatRoomDtoTable


class LoadedYoursChatRoomDtoTable(BaseSState[ChatRoomDtoTable]):
    @staticmethod
    def get_name() -> str:
        return "LOADED_YOURS_CHAT_ROOM_DTO_TABLE"
