from streamlit.delta_generator import DeltaGenerator


class ActionResults:
    def __init__(
        self,
        account_id: str,
        raw_password: str,
        message_area: DeltaGenerator,
        loading_area: DeltaGenerator,
        is_pushed: bool,
    ) -> None:
        self._account_id = account_id
        self._raw_password = raw_password
        self._message_area = message_area
        self._loading_area = loading_area
        self._is_pushed = is_pushed

    @property
    def account_id(self) -> str:
        return self._account_id

    @property
    def raw_password(self) -> str:
        return self._raw_password

    @property
    def message_area(self) -> DeltaGenerator:
        return self._message_area

    @property
    def loading_area(self) -> DeltaGenerator:
        return self._loading_area

    @property
    def is_pushed(self) -> bool:
        return self._is_pushed