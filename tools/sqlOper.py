from rsc.const import Const
import sqlite3
from datetime import datetime

_const = Const()
_id = _const.ColumnName.id
_name = _const.ColumnName.name
_value = _const.ColumnName.value
_date = _const.ColumnName.date
_comment = _const.ColumnName.comment
_scenario = _const.ColumnName.scenario
_bank = _const.TableName.bank
_cash = _const.TableName.cash
_user = _const.TableName.user
_first = _const.ClassName.first
_classification = _const.ColumnName.classification


class SqlOperation:

    def __init__(self, path="data/database.db"):
        self._connection = sqlite3.connect(path)
        self._cursor = self._connection.cursor()
        self._create_all_tables()

    def close(self):
        self._cursor.close()
        self._connection.close()

    def _create_all_tables(self):
        self._cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {_user} ("
            f"{_id} INTEGER PRIMARY KEY, "
            f"{_name} TEXT, "
            f"{_scenario} TEXT)")

        self._cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {_bank} ("
            f"{_id} INTEGER PRIMARY KEY, "
            f"{_value} INTEGER, "
            f"{_comment} TEXT, "
            f"{_name} TEXT, "
            f"{_classification} TEXT, "
            f"{_date} TEXT)")

        self._cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {_cash} ("
            f"{_id} INTEGER PRIMARY KEY, "
            f"{_value} INTEGER, "
            f"{_comment} TEXT)")

    def add_user(self, user_id: int, user_name: str):
        result = (user_id, user_name, _first)
        self._cursor.execute(f"INSERT OR IGNORE INTO {_user} VALUES (?, ?, ?)", result)
        self._connection.commit()

    def save_cash(self, user_id: int, value: str, comment: str):
        result = (user_id, value, comment)
        self._cursor.execute(f"INSERT OR IGNORE INTO {_cash} VALUES (?, ?, ?)", result)
        self._connection.commit()
        result = (value, comment, user_id)
        self._cursor.execute(f"UPDATE {_cash} SET {_value} = ?, {_comment} = ? WHERE {_id} = ?", result)
        self._connection.commit()

    def load_cash(self, user_id: int) -> (str, str):
        self._cursor.execute(f"SELECT * FROM {_cash} WHERE {_id} = ?", (user_id,))
        result = self._cursor.fetchone()
        return result[1], result[2]

    def get_user_status(self, user_id: int):
        self._cursor.execute(f"SELECT * FROM {_user} WHERE {_id} = ?", (user_id,))
        result = self._cursor.fetchone()
        result_dict = {
            _id: result[0],
            _name: result[1],
            _scenario: result[2],
        }
        return result_dict

    def set_user_status(self, user_id: int, scenario: str):
        result = scenario, user_id,
        self._cursor.execute(f"UPDATE {_user} SET {_scenario} = ? WHERE {_id} = ?", result)
        self._connection.commit()

    def add_transition(self, user_id: int, value: int, comment: str, classification: str):
        self._cursor.execute(f"SELECT MAX(id) FROM {_bank}")
        max_id = self._cursor.fetchone()[0]
        new_id = 1 if max_id is None else max_id + 1
        name = self.get_user_status(user_id)[_name]
        date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        result = new_id, value, comment, name, classification, date,
        self._cursor.execute(f"INSERT OR IGNORE INTO {_bank} VALUES (?,?,?,?,?,?)", result)
        self._connection.commit()

    def get_current_balance(self):
        self._cursor.execute(f'SELECT SUM({_value}) FROM {_bank};')
        current_balance = self._cursor.fetchone()[0]
        return current_balance

    def delete_transition(self, transition_id: int):
        query = f"DELETE FROM {_bank} WHERE {_id} = {transition_id}"
        self._cursor.execute(query)
        self._connection.commit()

    def get_transitions_count(self, count=10):
        self._cursor.execute(f"SELECT * FROM {_bank} ORDER BY {_id} DESC LIMIT {count}")
        rows = self._cursor.fetchall()
        text = [f"Баланс: {self.get_current_balance()}"]
        number_count = 0
        for element in rows:
            number_count += 1
            text.append(f"{number_count}.  {element[1]},  {element[2]},  {element[3]},  {element[4]}, {element[5]} ")
        return "\n".join(text)


class Sql:

    @staticmethod
    def add_user(user_id: int, user_name: str):
        _sqlClass = SqlOperation()
        _sqlClass.add_user(user_id=user_id, user_name=user_name)
        _sqlClass.close()

    @staticmethod
    def get_user_status(user_id: int):
        _sqlClass = SqlOperation()
        user_status = _sqlClass.get_user_status(user_id=user_id)
        _sqlClass.close()
        return user_status

    @staticmethod
    def set_user_status(user_id: int, scenario: str):
        _sqlClass = SqlOperation()
        _sqlClass.set_user_status(user_id=user_id, scenario=scenario)
        _sqlClass.close()

    @staticmethod
    def add_transition(user_id: int, value: int, comment: str, classification: str):
        _sqlClass = SqlOperation()
        _sqlClass.add_transition(user_id=user_id, value=value, comment=comment, classification=classification)
        _sqlClass.close()

    @staticmethod
    def get_current_balance():
        _sqlClass = SqlOperation()
        balance = _sqlClass.get_current_balance()
        _sqlClass.close()
        return balance

    @staticmethod
    def delete_transition(transition_id: int):
        _sqlClass = SqlOperation()
        _sqlClass.delete_transition(transition_id=transition_id)
        _sqlClass.close()

    @staticmethod
    def get_transitions_count(count=10):
        _sqlClass = SqlOperation()
        transitions = _sqlClass.get_transitions_count(count)
        _sqlClass.close()
        return transitions

    @staticmethod
    def save_cash(user_id: int, value: str, comment: str):
        _sqlClass = SqlOperation()
        _sqlClass.save_cash(user_id=user_id, value=value, comment=comment)
        _sqlClass.close()

    @staticmethod
    def load_cash(user_id: int) -> (str, str):
        _sqlClass = SqlOperation()
        cash = _sqlClass.load_cash(user_id=user_id)
        _sqlClass.close()
        return cash
