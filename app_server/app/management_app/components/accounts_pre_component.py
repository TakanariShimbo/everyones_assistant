from ..s_states import LoadAccountTableProcess, LoadedAccountTable, CurrentComponentEnity


class AccountsPreComponent:
    @staticmethod
    def init():
        LoadAccountTableProcess.init()

    @staticmethod
    def prepare():
        processer_manager = LoadAccountTableProcess.get()
        response = processer_manager.run_all()
        LoadedAccountTable.set(value=response.contents)
        CurrentComponentEnity.set_accounts_entity()

    @staticmethod
    def deinit():
        LoadAccountTableProcess.deinit()
