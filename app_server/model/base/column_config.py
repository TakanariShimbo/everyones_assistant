from pandas.api.extensions import ExtensionDtype


class ColumnConfig:
    def __init__(
        self,
        name: str,
        dtype: ExtensionDtype,
        unique: bool = False,
        non_null: bool = False,
        auto_assigned: bool = False,
    ):
        self._name = name
        self._dtype = dtype
        self._unique = unique
        self._non_null = non_null
        self._auto_assigned = auto_assigned

    @property
    def name(self) -> str:
        return self._name

    @property
    def dtype(self) -> ExtensionDtype:
        return self._dtype

    @property
    def unique(self) -> bool:
        return self._unique

    @property
    def non_null(self) -> bool:
        return self._non_null

    @property
    def auto_assigned(self) -> bool:
        return self._auto_assigned
