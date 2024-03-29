from typing import Optional

from streamlit.delta_generator import DeltaGenerator

from model import AssistantTypeEntity, ChatRoomEntity


class ReturnHomeActionResults:
    def __init__(
        self,
        loading_area: DeltaGenerator,
        is_pushed: bool,
    ) -> None:
        self._loading_area = loading_area
        self._is_pushed = is_pushed

    @property
    def loading_area(self) -> DeltaGenerator:
        return self._loading_area

    @property
    def is_pushed(self) -> bool:
        return self._is_pushed


class MenusActionResults:
    def __init__(
        self,
        loading_area: DeltaGenerator,
        is_pushed: bool,
    ) -> None:
        self._loading_area = loading_area
        self._is_pushed = is_pushed

    @property
    def loading_area(self) -> DeltaGenerator:
        return self._loading_area

    @property
    def is_pushed(self) -> bool:
        return self._is_pushed


class EnterActionResults:
    def __init__(
        self,
        chat_room_entity: ChatRoomEntity,
        loading_area: DeltaGenerator,
    ) -> None:
        self._chat_room_entity = chat_room_entity
        self._loading_area = loading_area

    @property
    def chat_room_entity(self) -> ChatRoomEntity:
        return self._chat_room_entity

    @property
    def loading_area(self) -> DeltaGenerator:
        return self._loading_area


class QueryActionResults:
    def __init__(
        self,
        assistant_entity: Optional[AssistantTypeEntity],
        prompt: str,
        message_area: DeltaGenerator,
        is_run_pushed: bool,
        is_rerun_pushed: bool,
        is_cancel_pushed: bool,
    ) -> None:
        self._assistant_entity = assistant_entity
        self._prompt = prompt
        self._message_area = message_area
        self._is_run_pushed = is_run_pushed
        self._is_rerun_pushed = is_rerun_pushed
        self._is_cancel_pushed = is_cancel_pushed

    @property
    def assistant_entity(self) -> Optional[AssistantTypeEntity]:
        return self._assistant_entity

    @property
    def prompt(self) -> str:
        return self._prompt

    @property
    def message_area(self) -> DeltaGenerator:
        return self._message_area

    @property
    def is_run_pushed(self) -> bool:
        return self._is_run_pushed

    @property
    def is_rerun_pushed(self) -> bool:
        return self._is_rerun_pushed

    @property
    def is_cancel_pushed(self) -> bool:
        return self._is_cancel_pushed
