from streamlit.delta_generator import DeltaGenerator


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


class UpdateInfoActionResults:
    def __init__(
        self,
        mail_address: str,
        family_name_en: str,
        given_name_en: str,
        family_name_jp: str,
        given_name_jp: str,
        raw_password: str,
        message_area: DeltaGenerator,
        loading_area: DeltaGenerator,
        is_pushed: bool,
    ) -> None:
        self._mail_address = mail_address
        self._family_name_en = family_name_en
        self._given_name_en = given_name_en
        self._family_name_jp = family_name_jp
        self._given_name_jp = given_name_jp
        self._raw_password = raw_password
        self._message_area = message_area
        self._loading_area = loading_area
        self._is_pushed = is_pushed

    @property
    def mail_address(self) -> str:
        return self._mail_address

    @property
    def family_name_en(self) -> str:
        return self._family_name_en

    @property
    def given_name_en(self) -> str:
        return self._given_name_en

    @property
    def family_name_jp(self) -> str:
        return self._family_name_jp

    @property
    def given_name_jp(self) -> str:
        return self._given_name_jp

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


class ChangePassActionResults:
    def __init__(
        self,
        current_raw_password: str,
        new_raw_password: str,
        new_raw_password_confirm: str,
        message_area: DeltaGenerator,
        loading_area: DeltaGenerator,
        is_pushed: bool,
    ) -> None:
        self._current_raw_password = current_raw_password
        self._new_raw_password = new_raw_password
        self._new_raw_password_confirm = new_raw_password_confirm
        self._message_area = message_area
        self._loading_area = loading_area
        self._is_pushed = is_pushed

    @property
    def current_raw_password(self) -> str:
        return self._current_raw_password

    @property
    def new_raw_password(self) -> str:
        return self._new_raw_password

    @property
    def new_raw_password_confirm(self) -> str:
        return self._new_raw_password_confirm

    @property
    def message_area(self) -> DeltaGenerator:
        return self._message_area

    @property
    def loading_area(self) -> DeltaGenerator:
        return self._loading_area

    @property
    def is_pushed(self) -> bool:
        return self._is_pushed
