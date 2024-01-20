from abc import ABC, abstractmethod
from typing import Any, Dict, Generic, List, Tuple, Type, TypeVar

from .processer import BaseProcesser
from model import BaseResponse


class EarlyStopProcessException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


R = TypeVar("R", bound=BaseResponse)


class BaseProcessersManager(Generic[R], ABC):
    def __init__(self, processer_classes: List[Type[BaseProcesser]]) -> None:
        self._processer_classes = processer_classes
        self._is_running = False
        self._inner_dict = {}
        self._outer_dict = {}

    def init_processers(self, init_is_running=True) -> None:
        self._processers = [processer_class() for processer_class in self._processer_classes]
        self._inner_dict = {}
        self._outer_dict = {}
        if init_is_running:
            self._is_running = False

    def run_all(self, **kwargs) -> R:
        is_running = self._is_running
        self._is_running = True

        # run pre-process
        if not is_running:
            self.init_processers(init_is_running=False)
            try:
                self._outer_dict, self._inner_dict = self._pre_process_for_starting(**kwargs)
            except EarlyStopProcessException as e:
                self._is_running = False
                return self._get_response_class()(is_success=False, message=str(e))
        else:
            self._outer_dict = self._pre_process_for_running(**kwargs)

        # run main-processes
        for processer in self._processers:
            processer.start_and_wait_to_complete(self._outer_dict, self._inner_dict)

        # run post-process
        response = self._post_process(self._outer_dict, self._inner_dict)

        self._is_running = False
        return response

    @abstractmethod
    def _pre_process_for_starting(self, **kwargs) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def _pre_process_for_running(self, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> R:
        raise NotImplementedError("Subclasses must implement this method")

    @staticmethod
    @abstractmethod
    def _get_response_class() -> Type[R]:
        raise NotImplementedError("Subclasses must implement this method")
