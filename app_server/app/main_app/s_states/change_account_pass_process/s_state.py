from .processer import ChangeAccountPassProcesser
from .processer_manager import ChangeAccountPassProcesserManager
from ....base import BaseSState


class ChangeAccountPassProcess(BaseSState[ChangeAccountPassProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "CHANGE_ACCOUNT_PASS_PROCESS"

    @staticmethod
    def get_default() -> ChangeAccountPassProcesserManager:
        return ChangeAccountPassProcesserManager([ChangeAccountPassProcesser])
