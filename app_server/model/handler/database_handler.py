from textwrap import dedent
from typing import Any, Dict, List, Optional, Tuple

import pandas as pd
from sqlalchemy import Engine, text, CursorResult


class DatabaseHandler:
    @staticmethod
    def execute_sql(
        database_engine: Engine,
        statement: str,
        parameters: Optional[Dict[str, Any]],
    ) -> CursorResult:
        with database_engine.connect() as conn:
            result = conn.execute(statement=text(statement), parameters=parameters)
            conn.commit()
        return result

    @staticmethod
    def execute_sqls(
        database_engine: Engine,
        statement_and_parameters_list: List[Tuple[str, Optional[Dict[str, Any]]]],
    ) -> List[CursorResult]:
        results = []
        with database_engine.connect() as conn:
            for statement, parameters in statement_and_parameters_list:
                result = conn.execute(statement=text(statement), parameters=parameters)
                results.append(result)
            conn.commit()
        return results

    @staticmethod
    def query_sql_on_pandas(
        database_engine: Engine,
        statement: str,
        parameters: Optional[Dict[str, Any]] = None,
        dtype_dict: Optional[Dict[str, Any]] = None,
    ) -> pd.DataFrame:
        return pd.read_sql_query(sql=text(statement), con=database_engine, params=parameters, dtype=dtype_dict)

    @staticmethod
    def get_select_sql(
        table_name: str,
        filter_conditions: List[str],
        order_condition: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Tuple[str, None]:
        condition_str = " AND ".join(filter_conditions)
        statement = f"SELECT * FROM {table_name} WHERE {condition_str}"
        if order_condition:
            statement += f" ORDER BY {order_condition}"
        if limit is not None:
            statement += f" LIMIT {limit}"
        return statement, None

    @classmethod
    def get_simple_select_sql(
        cls,
        table_name: str,
        column_name: str,
        value: Any,
        order_condition: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> Tuple[str, Dict[str, Any]]:
        filter_condition = f"{column_name} = :{column_name}"
        statement, _ = cls.get_select_sql(table_name=table_name, filter_conditions=[filter_condition], order_condition=order_condition, limit=limit)
        parameters = {column_name: value}
        return statement, parameters

    @staticmethod
    def get_insert_sql(
        table_name: str,
        insert_column_names: List[str],
        return_column_names: List[str],
    ) -> Tuple[str, None]:
        insert_values = [f":{name}" for name in insert_column_names]
        insert_names_str = ", ".join(insert_column_names)
        return_names_str = ", ".join(return_column_names)
        insert_values_str = ", ".join(insert_values)

        statement = dedent(
            f"""
            INSERT INTO {table_name} ({insert_names_str})
            VALUES ({insert_values_str})
            RETURNING {return_names_str};
            """
        )
        return statement, None

    @staticmethod
    def get_update_sql(
        table_name: str,
        key_column_name: str,
        non_key_column_names: List[str],
    ) -> Tuple[str, None]:
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
    def get_delete_sql(
        table_name: str,
        key_column_name: str,
        key_value: Any,
    ) -> Tuple[str, Dict[str, Any]]:
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
    def get_upsert_sql(
        table_name: str,
        key_column_name: str,
        non_key_column_names: List[str],
        record_dicts: List[Dict[str, Any]],
    ) -> Tuple[str, Dict[str, Any]]:
        column_names = [key_column_name] + non_key_column_names
        column_names_str = ", ".join(column_names)

        n_record = len(record_dicts)

        record_str_list = []
        parameters = {}
        for i in range(n_record):
            value_list = []
            for column_name in column_names:
                value = record_dicts[i][column_name]
                if pd.isna(value):
                    value_list.append(f"DEFAULT")
                    continue
                value_list.append(f":{column_name}_{i}")
                parameters[f"{column_name}_{i}"] = value
            record_str = ", ".join(value_list)
            record_str_list.append(f"({record_str})")
        records_str = ", ".join(record_str_list)

        update_column_names_str = ", ".join([f"{col} = EXCLUDED.{col}" for col in non_key_column_names])

        statement = f"""
            INSERT INTO {table_name} ({column_names_str}) 
            VALUES {records_str}
            ON CONFLICT ({key_column_name})
            DO UPDATE SET 
                {update_column_names_str};
        """

        return statement, parameters

    # @staticmethod
    # def get_upsert_sql(
    #     table_name: str,
    #     key_column_name: str,
    #     non_key_column_names: List[str],
    #     record_dicts: List[Dict[str, Any]],
    # ) -> Tuple[str, Dict[str, Any]]:
    #     column_names = [key_column_name] + non_key_column_names
    #     column_names_str = ", ".join(column_names)

    #     n_record = len(record_dicts)
    #     record_str_list = []
    #     for i in range(n_record):
    #         record_str = ", ".join([f":{column}_{i}" for column in column_names])
    #         record_str_list.append(f"({record_str})")
    #     records_str = ", ".join(record_str_list)

    #     update_column_names_str = ", ".join([f"{col} = EXCLUDED.{col}" for col in non_key_column_names])

    #     statement = f"""
    #         INSERT INTO {table_name} ({column_names_str}) 
    #         VALUES {records_str}
    #         ON CONFLICT ({key_column_name})
    #         DO UPDATE SET 
    #             {update_column_names_str};
    #     """

    #     parameters = {}
    #     for i in range(n_record):
    #         for column_name in column_names:
    #             parameters[f"{column_name}_{i}"] = record_dicts[i][column_name]

    #     return statement, parameters
