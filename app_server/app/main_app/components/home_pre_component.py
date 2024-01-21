from .. import s_states as SStates
from model import AccountEntity


class HomePreComponent:
    @staticmethod
    def init() -> None:
        SStates.CurrentComponentEntity.init()
        SStates.LoadChatRoomDtoTablesProcess.init()

    @staticmethod
    def prepare() -> None:
        processer_manager = SStates.LoadChatRoomDtoTablesProcess.get()
        chat_room_dto_tables = processer_manager.run_all()
        SStates.LoadedYoursChatRoomDtoTable.set(value=chat_room_dto_tables.contents.yours_chat_room_table)
        SStates.LoadedEveryoneChatRoomDtoTable.set(value=chat_room_dto_tables.contents.everyone_chat_room_table)
        SStates.CurrentComponentEntity.set_home_entity()

    @classmethod
    def prepare_for_sign_in(cls, signed_in_account_entity: AccountEntity) -> None:
        SStates.SignedInAccountEntity.set(value=signed_in_account_entity)
        cls.prepare()

    @staticmethod
    def deinit() -> None:
        SStates.LoadChatRoomDtoTablesProcess.deinit()
