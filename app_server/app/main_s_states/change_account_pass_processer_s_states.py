from .change_account_pass_processers import ChangeAccountPassProcesser, ChangeAccountPassProcesserManager
from ..base import BaseSState


class ChangeAccountPassProcesserSState(BaseSState[ChangeAccountPassProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "CHANGE_ACCOUNT_PASS_PROCESSER_MANAGER"

    @staticmethod
    def get_default() -> ChangeAccountPassProcesserManager:
        return ChangeAccountPassProcesserManager([ChangeAccountPassProcesser])
