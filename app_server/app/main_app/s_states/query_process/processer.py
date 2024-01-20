from typing import Dict, Any

import streamlit as st

from ...forms import QueryForm
from ....base import BaseProcesser
from controller import AssistantManager, ChatRoomManager
from model import ROLE_TYPE_TABLE, AccountEntity


class Processer(BaseProcesser[str]):
    def _main_process(self, inner_dict: Dict[str, Any]) -> None:
        form: QueryForm = inner_dict["form"]
        manager: ChatRoomManager = inner_dict["manager"]
        account: AccountEntity = inner_dict["account"]
        answer = AssistantManager.query_streamly_answer_and_display(
            prompt=form.prompt,
            provider_id=form.provider_id,
            ai_model_id=form.ai_model_id,
            callback_func=self.add_queue,
            message_entities=manager.get_all_message_entities(),
        )
        manager.add_prompt_and_answer(
            prompt=form.prompt,
            answer=answer,
            account_id=account.account_id,
            assistant_id=form.assistant_id,
        )
        inner_dict["answer"] = answer

    def _pre_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        form: QueryForm = inner_dict["form"]
        with outer_dict["history_area"]:
            with st.chat_message(name=ROLE_TYPE_TABLE.USER_ID):
                st.write(form.prompt)
            with st.chat_message(name=ROLE_TYPE_TABLE.ASSISTANT_ID):
                outer_dict["answer_area"] = st.empty()

    def _post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        outer_dict["answer_area"].write(inner_dict["answer"])

    def _callback_process(self, content: str, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        outer_dict["answer_area"].write(content)
