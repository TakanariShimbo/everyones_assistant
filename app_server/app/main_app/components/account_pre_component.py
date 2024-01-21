from .. import s_states as SStates


class AccountPreComponent:
    @staticmethod
    def init() -> None:
        SStates.CurrentComponentEntity.init()

    @staticmethod
    def prepare() -> None:
        SStates.CurrentComponentEntity.set_account_entity()

    @staticmethod
    def deinit() -> None:
        pass
