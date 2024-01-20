from abc import ABC, abstractmethod
from threading import Thread
from typing import Any, Dict, Generic, TypeVar

from .queues import QueueHandler


T = TypeVar("T")


class BaseProcesser(Generic[T], Thread, ABC):
    def __init__(self, timeout_sec: float = 1.0) -> None:
        super().__init__()
        self._queue_handler = QueueHandler[T](timeout_sec)
        self._has_inner_dict = False

    def add_queue(self, content: T, is_finish: bool = False):
        self._queue_handler.send(content=content, is_finish=is_finish)

    def start_and_wait_to_complete(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        self._outer_dict = outer_dict
        if not self._has_inner_dict:
            self._inner_dict = inner_dict
            self._has_inner_dict = True

        self._pre_process(self._outer_dict, self._inner_dict)

        try:
            self.start()
        except RuntimeError:
            pass
        finally:
            while True:
                if not self.is_alive():
                    break
                response = self._queue_handler.receive()
                if response is None:
                    continue
                self._callback_process(response.content, self._outer_dict, self._inner_dict)
                if response.is_finish:
                    break
            self.join()

        self._post_process(self._outer_dict, self._inner_dict)

    def run(self) -> None:
        self._main_process(self._inner_dict)

    @abstractmethod
    def _main_process(self, inner_dict: Dict[str, Any]) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def _pre_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @abstractmethod
    def _callback_process(self, content: T, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        raise NotImplementedError("Subclasses must implement this method")
