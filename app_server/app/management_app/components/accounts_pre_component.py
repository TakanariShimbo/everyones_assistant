from .. import s_states as SStates


class AccountsPreComponent:
    @staticmethod
    def init() -> None:
        SStates.CurrentComponentEntity.init()
        SStates.LoadAccountTableProcess.init()

    @staticmethod
    def prepare() -> None:
        processer_manager = SStates.LoadAccountTableProcess.get()
        response = processer_manager.run_all()
        SStates.CurrentComponentEntity.set_accounts_entity()

    @staticmethod
    def deinit() -> None:
        SStates.LoadAccountTableProcess.deinit()
