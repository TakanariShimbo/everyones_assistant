from sqlalchemy import create_engine

from .static import LoadedEnv


class Database:
    url = f"{LoadedEnv.database_type}://{LoadedEnv.database_user}:{LoadedEnv.database_password}@{LoadedEnv.database_host}:{LoadedEnv.database_port}/{LoadedEnv.database_db}"
    engine = create_engine(url=url)