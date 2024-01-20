from ..s_states import LoadAccountsProcesserSState, AccountTableSState, ManagementComponentSState


class AccountsPreComponent:
    @staticmethod
    def init():
        LoadAccountsProcesserSState.init()

    @staticmethod
    def prepare():
        processer_manager = LoadAccountsProcesserSState.get()
        response = processer_manager.run_all()
        AccountTableSState.set(value=response.contents)
        ManagementComponentSState.set_accounts_entity()

    @staticmethod
    def deinit():
        LoadAccountsProcesserSState.deinit()
