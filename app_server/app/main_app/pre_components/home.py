from .. import s_states as SStates


class HomePreComponent:
    @staticmethod
    def init() -> None:
        SStates.CurrentComponentEntity.init()
        SStates.EnterMainHomeProcess.init()

    @staticmethod
    def prepare() -> None:
        processer_manager = SStates.EnterMainHomeProcess.get()
        processer_manager.run_all()
        SStates.CurrentComponentEntity.set_home_entity()

    @staticmethod
    def deinit() -> None:
        SStates.EnterMainHomeProcess.deinit()
