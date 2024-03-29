from abc import ABC, abstractmethod
from typing import TypeVar, Generic

import streamlit as st


T = TypeVar("T")


class BaseSState(Generic[T], ABC):
    @classmethod
    def get(cls) -> T:
        return st.session_state[cls.get_name()]

    @classmethod
    def set(cls, value: T) -> None:
        st.session_state[cls.get_name()] = value

    @classmethod
    def deinit(cls) -> None:
        if not cls.get_name() in st.session_state:
            del st.session_state[cls.get_name()]

    @staticmethod
    @abstractmethod
    def get_name() -> str:
        raise NotImplementedError("Subclasses must implement this method")


class BaseSStateNoDefault(BaseSState[T], ABC):
    @classmethod
    def validate(cls) -> None:
        if not cls.get_name() in st.session_state:
            raise ValueError("SState has not set yet.")


class BaseSStateHasDefault(BaseSState[T], ABC):
    @classmethod
    def reset(cls) -> None:
        cls.set(value=cls.get_default())

    @classmethod
    def init(cls) -> None:
        if not cls.get_name() in st.session_state:
            cls.reset()

    @staticmethod
    @abstractmethod
    def get_default() -> T:
        raise NotImplementedError("Subclasses must implement this method")
