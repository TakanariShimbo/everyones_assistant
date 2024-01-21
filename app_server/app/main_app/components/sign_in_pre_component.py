from .. import s_states as SStates


class SignInPreComponent:
    @staticmethod
    def init() -> None:
        SStates.CurrentComponentEntity.init()

    @staticmethod
    def prepare() -> None:
        SStates.SignedInAccountEntity.deinit()
        SStates.CurrentComponentEntity.set_sign_in_entity()

    @staticmethod
    def deinit() -> None:
        pass
