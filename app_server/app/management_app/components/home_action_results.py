from streamlit.delta_generator import DeltaGenerator


class ActionResults:
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
