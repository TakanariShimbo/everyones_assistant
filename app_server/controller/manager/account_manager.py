from model import Database, BaseResponse, AccountEntity


class SignUpResponse(BaseResponse[None]):
    pass


class SignInResponse(BaseResponse[AccountEntity]):
    pass


class UpdateInfoResponse(BaseResponse[AccountEntity]):
    pass


class ChangePassResponse(BaseResponse[AccountEntity]):
    pass


class AccountManager:
    @staticmethod
    def sign_up(
        account_id: str,
        mail_address: str,
        family_name_en: str,
        given_name_en: str,
        family_name_jp: str,
        given_name_jp: str,
        raw_password: str,
    ) -> SignUpResponse:
        new_account_entity = AccountEntity.init_with_hashing_password(
            account_id=account_id,
            mail_address=mail_address,
            family_name_en=family_name_en,
            given_name_en=given_name_en,
            family_name_jp=family_name_jp,
            given_name_jp=given_name_jp,
            raw_password=raw_password,
        )

        try:
            new_account_entity.save_to_database(database_engine=Database.ENGINE)
        except:
            return SignUpResponse(is_success=False, message=f"Account ID '{account_id}' has already signed up.")

        return SignUpResponse(is_success=True, message=f"Account ID '{account_id}' signed up correctly.")

    @staticmethod
    def sign_in(account_id: str, raw_password: str) -> SignInResponse:
        try:
            target_account_entity = AccountEntity.load_specified_id_from_database(database_engine=Database.ENGINE, account_id=account_id)
        except ValueError:
            return SignInResponse(is_success=False, message=f"Account ID '{account_id}' hasn't signed up yet.")

        if target_account_entity.is_disabled:
            return SignInResponse(is_success=False, message=f"Account ID '{account_id}' is disabled.")

        if not target_account_entity.verify_password(raw_password=raw_password):
            return SignInResponse(is_success=False, message=f"Please input password correctly.")

        return SignInResponse(is_success=True, contents=target_account_entity)

    @staticmethod
    def update_info(
        account_id: str,
        mail_address: str,
        family_name_en: str,
        given_name_en: str,
        family_name_jp: str,
        given_name_jp: str,
        raw_password: str,
    ) -> UpdateInfoResponse:
        try:
            target_account_entity = AccountEntity.load_specified_id_from_database(database_engine=Database.ENGINE, account_id=account_id)
        except:
            return UpdateInfoResponse(is_success=False, message=f"Account ID '{account_id}' hasn't signed up yet.")

        if not target_account_entity.verify_password(raw_password=raw_password):
            return UpdateInfoResponse(is_success=False, message=f"Please input password correctly.")

        target_account_entity.mail_address = mail_address
        target_account_entity.family_name_en = family_name_en
        target_account_entity.given_name_en = given_name_en
        target_account_entity.family_name_jp = family_name_jp
        target_account_entity.given_name_jp = given_name_jp

        try:
            target_account_entity.save_to_database(database_engine=Database.ENGINE, mode="update")
        except:
            return UpdateInfoResponse(is_success=False, message=f"Account ID '{account_id}' hasn't signed up yet.")

        return UpdateInfoResponse(is_success=True, message=f"Infomation of account ID '{account_id}' updated correctly.", contents=target_account_entity)

    @staticmethod
    def change_password(
        account_id: str,
        current_raw_password: str,
        new_raw_password: str,
    ) -> ChangePassResponse:
        try:
            target_account_entity = AccountEntity.load_specified_id_from_database(database_engine=Database.ENGINE, account_id=account_id)
        except:
            return ChangePassResponse(is_success=False, message=f"Account ID '{account_id}' hasn't signed up yet.")

        if not target_account_entity.set_new_password(raw_password=current_raw_password, new_raw_password=new_raw_password):
            return ChangePassResponse(is_success=False, message=f"Please input current password correctly.")

        try:
            target_account_entity.save_to_database(database_engine=Database.ENGINE, mode="update")
        except:
            return ChangePassResponse(is_success=False, message=f"Account ID '{account_id}' hasn't signed up yet.")

        return ChangePassResponse(is_success=True, message=f"Password of account ID '{account_id}' updated correctly.", contents=target_account_entity)
