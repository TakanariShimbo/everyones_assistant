from typing import Optional

from streamlit.delta_generator import DeltaGenerator

from model import AssistantTypeEntity


class ActionResults:
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