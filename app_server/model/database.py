from sqlalchemy import create_engine

from .static import LoadedEnv


class Database:
    URL = f"{LoadedEnv.DATABASE_TYPE}://{LoadedEnv.DATABASE_USER}:{LoadedEnv.DATABASE_PASSWORD}@{LoadedEnv.DATABASE_HOST}:{LoadedEnv.DATABASE_PORT}/{LoadedEnv.DATABASE_DB}"
    ENGINE = create_engine(url=URL)