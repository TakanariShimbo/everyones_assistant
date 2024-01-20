from .. import s_states as SStates


class SignInPreComponent:
    @staticmethod
    def init() -> None:
        SStates.CurrentComponentEnity.init()

    @staticmethod
    def prepare() -> None:
        SStates.CurrentComponentEnity.set_sign_in_entity()

    @staticmethod
    def deinit() -> None:
        pass
