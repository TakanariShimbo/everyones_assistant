from textwrap import dedent
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd
from sqlalchemy import Engine, text, CursorResult


class DatabaseHandler:
    @staticmethod
    def execute_sql(database_engine: Engine, statement: str, parameters: Optional[Dict[str, Any]]) -> CursorResult:
        with database_engine.connect() as conn:
            result = conn.execute(statement=text(statement), parameters=parameters)
            conn.commit()
        return result

    @staticmethod
    def execute_sqls(database_engine: Engine, statement_and_parameters_list: List[Tuple[str, Optional[Dict[str, Any]]]]) -> List[CursorResult]:
        results = []
        with database_engine.connect() as conn:
            for statement, parameters in statement_and_parameters_list:
                result = conn.execute(statement=text(statement), parameters=parameters)
                results.append(result)
            conn.commit()
        return results

    @staticmethod
    def query_sql_on_pandas(database_engine: Engine, statement: str, parameters: Optional[Dict[str, Any]] = None, dtype_dict: Optional[Dict[str, Any]] = None) -> pd.DataFrame:
        return pd.read_sql_query(sql=text(statement), con=database_engine, params=parameters, dtype=dtype_dict)

    @staticmethod
    def get_select_sql(table_name: str, filter_conditions: List[str], order_condition: Optional[str] = None, limit: Optional[int] = None) -> Tuple[str, None]:
        condition_str = " AND ".join(filter_conditions)
        statement = f"SELECT * FROM {table_name} WHERE {condition_str}"
        if order_condition:
            statement += f" ORDER BY {order_condition}"
        if limit is not None:
            statement += f" LIMIT {limit}"
        return statement, None

    @classmethod
    def get_simple_select_sql(cls, table_name: str, column_name: str, value: Any, order_condition: Optional[str] = None, limit: Optional[int] = None) -> Tuple[str, Dict[str, Any]]:
        filter_condition = f"{column_name} = :{column_name}"
        statement, _ = cls.get_select_sql(table_name=table_name, filter_conditions=[filter_condition], order_condition=order_condition, limit=limit)
        parameters = {column_name: value}
        return statement, parameters

    @staticmethod
    def get_insert_sql(table_name: str, column_names: List[str]) -> Tuple[str, None]:
        values = [f":{name}" for name in column_names]
        column_names_str = ", ".join(column_names)
        values_str = ", ".join(values)

        statement = dedent(
            f"""
            INSERT INTO {table_name} ({column_names_str})
            VALUES ({values_str});
            """
        )
        return statement, None

    @staticmethod
    def get_update_sql(table_name: str, key_column_name: str, non_key_column_names: List[str]) -> Tuple[str, None]:
        key_name_and_value_str = f"{key_column_name} = :{key_column_name}"
        non_key_name_and_values = [f"{name} = :{name}" for name in non_key_column_names]
        name_and_values_str = ", ".join(non_key_name_and_values)

        statement = dedent(
            f"""
            UPDATE {table_name}
            SET {name_and_values_str}
            WHERE {key_name_and_value_str};
            """
        )
        return statement, None

    @staticmethod
    def get_delete_sql(table_name: str, key_column_name: str, key_value: Any) -> Tuple[str, Dict[str, Any]]:
        condition_str = f"{key_column_name} = :{key_column_name}"

        statement = dedent(
            f"""
            DELETE FROM {table_name}
            WHERE {condition_str};
            """
        )
        parameters = {key_column_name: key_value}
        return statement, parameters

    @staticmethod
    def get_truncate_sql(table_name: str) -> Tuple[str, None]:
        statement = f"TRUNCATE TABLE {table_name};"
        parameters = None
        return statement, parameters
    
    @staticmethod
    def get_upsert_sql(table_name: str, temp_table_name: str, key_column_name: str, non_key_column_names: List[str]) -> Tuple[str, None]:
        """
        NOTES: KEY COLUMN MUST BE 'AUTO_ASSIGNED'=FALSE.
        """
        column_names_str = ", ".join([key_column_name] + non_key_column_names)
        update_column_names_str = ", ".join([f"{col} = EXCLUDED.{col}" for col in non_key_column_names])

        statement = dedent(
            f"""
            INSERT INTO {table_name} ({column_names_str})
            SELECT {column_names_str}
            FROM {temp_table_name}
            ON CONFLICT ({key_column_name}) 
            DO UPDATE SET 
                {update_column_names_str}
            """
        )
        parameters = None
        return statement, parameters