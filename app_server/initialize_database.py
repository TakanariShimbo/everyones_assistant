from model import Database, AccountConfig, ChatRoomConfig, ChatMessageConfig, AccountEntity, LoadedEnv


"""
CREATE TABLES
"""
AccountConfig.create_table_on_database(database_engine=Database.ENGINE)
ChatRoomConfig.create_table_on_database(database_engine=Database.ENGINE)
ChatMessageConfig.create_table_on_database(database_engine=Database.ENGINE)


"""
CREATE ADMIN_ACCOUNT
"""
admin_account_entity = AccountEntity.init_with_hashing_password(
    account_id=LoadedEnv.ADMIN_ID,
    mail_address="admin@dummy.co.jp",
    family_name_en="administrative",
    given_name_en="account",
    family_name_jp="管理者",
    given_name_jp="アカウント",
    raw_password=LoadedEnv.ADMIN_PASSWORD,
    is_user=False,
    is_administrator=True,
)
admin_account_entity = admin_account_entity.insert_record_to_database(database_engine=Database.ENGINE)
