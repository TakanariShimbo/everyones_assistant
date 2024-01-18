from streamlit.delta_generator import DeltaGenerator


class ActionResults:
    def __init__(
        self,
        admin_id: str,
        admin_password: str,
        message_area: DeltaGenerator,
        is_pushed: bool,
    ) -> None:
        self._admin_id = admin_id
        self._admin_password = admin_password
        self._message_area = message_area
        self._is_pushed = is_pushed

    @property
    def admin_id(self) -> str:
        return self._admin_id

    @property
    def admin_password(self) -> str:
        return self._admin_password

    @property
    def message_area(self) -> DeltaGenerator:
        return self._message_area

    @property
    def is_pushed(self) -> bool:
        return self._is_pushed