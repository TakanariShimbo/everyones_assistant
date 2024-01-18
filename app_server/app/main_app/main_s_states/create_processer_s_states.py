from .create_processers import CreateProcesser, CreateProcesserManager
from ...base import BaseSState


class CreateProcesserSState(BaseSState[CreateProcesserManager]):
    @staticmethod
    def get_name() -> str:
        return "CREATE_PROCESSER_MANAGER"

    @staticmethod
    def get_default() -> CreateProcesserManager:
        return CreateProcesserManager([CreateProcesser])

