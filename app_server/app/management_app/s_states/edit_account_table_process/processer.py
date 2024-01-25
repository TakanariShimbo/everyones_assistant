from typing import Dict, Any

from ....base import BaseProcesser
from model import Database, AccountTable


class Processer(BaseProcesser[None]):
    def _main_process(self, inner_dict: Dict[str, Any]) -> None:
        account_table: AccountTable = inner_dict["table"]
        edited_display_df = inner_dict["edited_display_df"]

        only_edited_table = account_table.get_only_edited_table(edited_display_df=edited_display_df)
        only_edited_table.update_records_of_database(database_engine=Database.ENGINE)

    def _pre_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass

    def _callback_process(self, content: None, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        pass
