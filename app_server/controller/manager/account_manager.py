from model import DATABASE_ENGINE, BaseResponse, AccountEntity


class SignUpResponse(BaseResponse[None]):
    pass

class SignInResponse(BaseResponse[AccountEntity]):
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
            new_account_entity.save_to_database(database_engine=DATABASE_ENGINE)
        except:
            return SignUpResponse(is_success=False, message=f"Account ID '{account_id}' has already signed up.")

        return SignUpResponse(is_success=True, message=f"Account ID '{account_id}' signed up correctly.")

    @staticmethod
    def sign_in(account_id: str, raw_password: str) -> SignInResponse:
        try:
            target_account_entity = AccountEntity.load_specified_id_from_database(database_engine=DATABASE_ENGINE, account_id=account_id)
        except ValueError:
            return SignInResponse(is_success=False, message=f"Account ID '{account_id}' hasn't signed up yet.")

        if not target_account_entity.verify_password(raw_password=raw_password):
            return SignInResponse(is_success=False, message=f"Please input password correctly.")
        
        return SignInResponse(is_success=True, contents=target_account_entity)