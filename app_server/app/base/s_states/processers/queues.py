from queue import Queue, Empty
from typing import Generic, Optional, TypeVar


T = TypeVar("T")


class QueueResponse(Generic[T]):
    def __init__(self, content: T, is_finish: bool = False) -> None:
        self._content = content
        self._is_finish = is_finish

    @property
    def content(self) -> T:
        return self._content

    @property
    def is_finish(self) -> bool:
        return self._is_finish

    def __str__(self) -> str:
        return str(self._content)


class QueueHandler(Generic[T]):
    def __init__(self, timeout_sec: float = 1) -> None:
        self._queue = Queue()
        self._timeout_sec = timeout_sec

    def send(self, content: T, is_finish: bool = False) -> None:
        response = QueueResponse[T](content, is_finish)
        self._queue.put(response)

    def receive(self) -> Optional[QueueResponse[T]]:
        try:
            return self._queue.get(timeout=self._timeout_sec)
        except Empty:
            return None
