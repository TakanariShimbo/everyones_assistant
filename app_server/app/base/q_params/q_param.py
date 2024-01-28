from abc import ABC, abstractmethod

import streamlit as st


class BaseQParam(ABC):
    @classmethod
    def get(cls) -> str:
        return st.query_params[cls.get_name()]

    @classmethod
    def set(cls, value: str) -> None:
        st.query_params[cls.get_name()] = value

    @classmethod
    def deinit(cls) -> None:
        if not cls.get_name() in st.query_params:
            del st.query_params[cls.get_name()]

    @staticmethod
    @abstractmethod
    def get_name() -> str:
        raise NotImplementedError("Subclasses must implement this method")


class BaseQParamNoDefault(BaseQParam, ABC):
    @classmethod
    def validate(cls) -> None:
        if not cls.get_name() in st.query_params:
            raise ValueError("QParams has not set yet.")


class BaseQParamHasDefault(BaseQParam, ABC):
    @classmethod
    def reset(cls) -> None:
        cls.set(value=cls.get_default())

    @classmethod
    def init(cls) -> None:
        if not cls.get_name() in st.query_params:
            cls.reset()

    @staticmethod
    @abstractmethod
    def get_default() -> str:
        raise NotImplementedError("Subclasses must implement this method")
