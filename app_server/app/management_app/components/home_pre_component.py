from .. import s_states as SStates


class HomePreComponent:
    @staticmethod
    def init() -> None:
        SStates.CurrentComponentEntity.init()

    @staticmethod
    def prepare() -> None:
        SStates.CurrentComponentEntity.set_home_entity()

    @staticmethod
    def deinit() -> None:
        pass