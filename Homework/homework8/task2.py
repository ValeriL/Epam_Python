import sqlite3
from typing import Any, Callable, Tuple


def database_connection(func: Callable):
    def wrapper(self, *args, **kwargs):
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
            return func(self, cursor, *args, **kwargs)

    return wrapper


class TableData:
    def __init__(self, database_name: str, table_name: str):
        self.database_name = database_name
        self.table_name = table_name

    @database_connection
    def __len__(self, cursor) -> int:  # noqa: S608
        cursor.execute(f"SELECT COUNT(*) FROM {self.table_name}")
        return cursor.fetchone()[0]

    @database_connection
    def __getitem__(self, cursor, item: str) -> Tuple[Any]:
        cursor.execute(
            f"SELECT * FROM  {self.table_name} WHERE name=:item",
            {"item": item},  # noqa: S608
        )
        row = cursor.fetchone()
        if not row:
            raise KeyError(f"{item} not found")
        return row

    @database_connection
    def __contains__(self, cursor, item: str) -> bool:
        try:
            self[item]
        except KeyError:
            return False
        else:
            return True

    @database_connection
    def __iter__(self, cursor) -> Tuple:  # noqa: S608
        yield from cursor.execute(f"SELECT * FROM {self.table_name}")
