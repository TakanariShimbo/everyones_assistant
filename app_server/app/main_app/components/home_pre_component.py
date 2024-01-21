from .. import s_states as SStates


class HomePreComponent:
    @staticmethod
    def init() -> None:
        SStates.CurrentComponentEntity.init()
        SStates.LoadChatRoomDtoTablesProcess.init()

    @staticmethod
    def prepare() -> None:
        processer_manager = SStates.LoadChatRoomDtoTablesProcess.get()
        processer_manager.run_all()
        SStates.CurrentComponentEntity.set_home_entity()

    @staticmethod
    def deinit() -> None:
        SStates.LoadChatRoomDtoTablesProcess.deinit()
