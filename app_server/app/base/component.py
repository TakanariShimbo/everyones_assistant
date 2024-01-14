from abc import ABC, abstractmethod


class BaseComponent(ABC):
    @classmethod
    def run(cls) -> None:
        cls.init()
        cls.main()

    @staticmethod
    @abstractmethod
    def init() -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @classmethod
    @abstractmethod
    def main(cls) -> None:
        raise NotImplementedError("Subclasses must implement this method")

    @staticmethod
    @abstractmethod
    def deinit() -> None:
        raise NotImplementedError("Subclasses must implement this method")
