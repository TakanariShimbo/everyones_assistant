from .. import s_states as SStates


class HomePreComponent:
    @staticmethod
    def init() -> None:
        SStates.CurrentComponentEnity.init()

    @staticmethod
    def prepare() -> None:
        SStates.CurrentComponentEnity.set_home_entity()

    @staticmethod
    def deinit() -> None:
        pass