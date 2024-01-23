from ...base import BaseSStateNoDefault
from controller import MainHomeManager


class LoadedMainHomeManager(BaseSStateNoDefault[MainHomeManager]):
    @staticmethod
    def get_name() -> str:
        return "LOADED_MAIN_HOME_MANAGER"
