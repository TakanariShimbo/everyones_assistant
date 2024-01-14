from typing import Dict, Any, Tuple

import streamlit as st

from ..main_forms import QueryForm
from .account_s_states import AccountSState
from .chat_room_s_states import ChatRoomSState
from ..base import BaseProcesser, BaseProcessersManager, EarlyStopProcessException
from controller import AssistantManager, ChatRoomManager
from model import ROLE_TYPE_TABLE, AccountEntity


class QueryProcesser(BaseProcesser[str]):
    def main_process(self, inner_dict: Dict[str, Any]) -> None:
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

    def pre_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        form: QueryForm = inner_dict["form"]
        with outer_dict["history_area"]:
            with st.chat_message(name=ROLE_TYPE_TABLE.user_id):
                st.write(form.prompt)
            with st.chat_message(name=ROLE_TYPE_TABLE.assistant_id):
                outer_dict["answer_area"] = st.empty()

    def post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        outer_dict["answer_area"].write(inner_dict["answer"])

    def callback_process(self, content: str, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> None:
        outer_dict["answer_area"].write(content)


class QueryProcesserManager(BaseProcessersManager):
    def pre_process_for_starting(self, **kwargs) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]
        outer_dict["history_area"] = kwargs["history_area"]

        try:
            inner_dict = {}
            inner_dict["form"] = QueryForm.from_entity(assistant_entity=kwargs["assistant_entity"], prompt=kwargs["prompt"])
            inner_dict["manager"] = ChatRoomSState.get()
            inner_dict["account"] = AccountSState.get()
        except:
            outer_dict["message_area"].warning("Please input form corectly.")
            raise EarlyStopProcessException()
        return outer_dict, inner_dict

    def pre_process_for_running(self, **kwargs) -> Dict[str, Any]:
        outer_dict = {}
        outer_dict["message_area"] = kwargs["message_area"]
        outer_dict["history_area"] = kwargs["history_area"]

        kwargs["message_area"].warning("Running.")
        return outer_dict

    def post_process(self, outer_dict: Dict[str, Any], inner_dict: Dict[str, Any]) -> bool:
        outer_dict["message_area"].empty()
        return True
