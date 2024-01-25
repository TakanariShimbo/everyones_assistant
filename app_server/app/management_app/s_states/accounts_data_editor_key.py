from ...base import BaseSStateHasDefault


class AccountsDataEditorKey(BaseSStateHasDefault[int]):
    @staticmethod
    def get_name() -> str:
        return "ACCOUNTS_DATA_EDITOR_KEY"
    
    @staticmethod
    def get_default() -> int:
        return 0

    @classmethod
    def change_key(cls):
        val = cls.get()
        new_val = (val + 1) % 2
        cls.set(value=new_val)
