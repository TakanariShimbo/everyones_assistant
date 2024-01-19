from abc import ABC, abstractmethod


class BasePreComponent(ABC):
    @classmethod
    def run(cls) -> None:
        cls.main()

    @classmethod
    @abstractmethod
    def main(cls) -> None:
        raise NotImplementedError("Subclasses must implement this method")
