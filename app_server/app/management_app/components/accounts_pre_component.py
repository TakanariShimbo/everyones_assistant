from .. import s_states as SStates


class AccountsPreComponent:
    @staticmethod
    def init() -> None:
        SStates.CurrentComponentEnity.init()
        SStates.LoadAccountTableProcess.init()

    @staticmethod
    def prepare() -> None:
        processer_manager = SStates.LoadAccountTableProcess.get()
        response = processer_manager.run_all()
        loaded_account_table = response.contents
        SStates.LoadedAccountTable.set(value=loaded_account_table)
        SStates.CurrentComponentEnity.set_accounts_entity()

    @staticmethod
    def deinit() -> None:
        SStates.LoadAccountTableProcess.deinit()
