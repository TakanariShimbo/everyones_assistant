import pandas as pd
from streamlit.delta_generator import DeltaGenerator


class SignUpActionResults:
    def __init__(
        self,
        account_id: str,
        mail_address: str,
        family_name_en: str,
        given_name_en: str,
        family_name_jp: str,
        given_name_jp: str,
        raw_password: str,
        raw_password_confirm: str,
        message_area: DeltaGenerator,
        loading_area: DeltaGenerator,
        is_pushed: bool,
    ) -> None:
        self._account_id = account_id
        self._mail_address = mail_address
        self._family_name_en = family_name_en
        self._given_name_en = given_name_en
        self._family_name_jp = family_name_jp
        self._given_name_jp = given_name_jp
        self._raw_password = raw_password
        self._raw_password_confirm = raw_password_confirm
        self._message_area = message_area
        self._loading_area = loading_area
        self._is_pushed = is_pushed

    @property
    def account_id(self) -> str:
        return self._account_id

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
    def raw_password_confirm(self) -> str:
        return self._raw_password_confirm

    @property
    def message_area(self) -> DeltaGenerator:
        return self._message_area

    @property
    def loading_area(self) -> DeltaGenerator:
        return self._loading_area

    @property
    def is_pushed(self) -> bool:
        return self._is_pushed


class EditAccountsActionResults:
    def __init__(
        self,
        loading_area: DeltaGenerator,
        is_update_pushed: bool,
        is_load_pushed: bool,
        edited_display_df: pd.DataFrame,
    ) -> None:
        self._loading_area = loading_area
        self._is_update_pushed = is_update_pushed
        self._is_load_pushed = is_load_pushed
        self._edited_display_df = edited_display_df

    @property
    def loading_area(self) -> DeltaGenerator:
        return self._loading_area

    @property
    def is_update_pushed(self) -> bool:
        return self._is_update_pushed

    @property
    def is_load_pushed(self) -> bool:
        return self._is_load_pushed

    @property
    def edited_display_df(self) -> pd.DataFrame:
        return self._edited_display_df
