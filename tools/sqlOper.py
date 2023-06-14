from rsc.container import Container
import sqlite3
from datetime import datetime

container = Container()


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
            f"CREATE TABLE IF NOT EXISTS {container.TableName.user} ("
            f"{container.ColumnName.id} INTEGER PRIMARY KEY, "
            f"{container.ColumnName.name} TEXT, "
            f"{container.ColumnName.scenario} TEXT)")

        self._cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {container.TableName.bank} ("
            f"{container.ColumnName.id} INTEGER PRIMARY KEY, "
            f"{container.ColumnName.value} INTEGER, "
            f"{container.ColumnName.comment} TEXT, "
            f"{container.ColumnName.name} TEXT, "
            f"{container.ColumnName.classification} TEXT, "
            f"{container.ColumnName.date} TEXT)")

        self._cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {container.TableName.cash} ("
            f"{container.ColumnName.id} INTEGER PRIMARY KEY, "
            f"{container.ColumnName.value} INTEGER, "
            f"{container.ColumnName.comment} TEXT)")

    def add_user(self, user_id: int, user_name: str):
        result = (user_id, user_name, container.Config.default_scenario)
        self._cursor.execute(f"INSERT OR IGNORE INTO {container.TableName.user} VALUES (?, ?, ?)", result)
        self._connection.commit()

    def save_cash(self, user_id: int, value: str, comment: str):
        result = (user_id, value, comment)
        self._cursor.execute(f"INSERT OR IGNORE INTO {container.TableName.cash} VALUES (?, ?, ?)", result)
        self._connection.commit()
        result = (value, comment, user_id)
        self._cursor.execute(f"UPDATE {container.TableName.cash} SET {container.ColumnName.value} = ?, "
                             f"{container.ColumnName.comment} = ? WHERE {container.ColumnName.id} = ?", result)
        self._connection.commit()

    def load_cash(self, user_id: int) -> (str, str):
        self._cursor.execute(f"SELECT * FROM {container.TableName.cash} "
                             f"WHERE {container.ColumnName.id} = ?", (user_id,))
        result = self._cursor.fetchone()
        return result[1], result[2]

    def get_user_status(self, user_id: int):
        self._cursor.execute(f"SELECT * FROM {container.TableName.user} "
                             f"WHERE {container.ColumnName.id} = ?", (user_id,))
        result = self._cursor.fetchone()
        result_dict = {
            container.ColumnName.id: result[0],
            container.ColumnName.name: result[1],
            container.ColumnName.scenario: result[2],
        }
        return result_dict

    def set_user_status(self, user_id: int, scenario: str):
        result = scenario, user_id,
        self._cursor.execute(f"UPDATE {container.TableName.user} SET {container.ColumnName.scenario} = ? "
                             f"WHERE {container.ColumnName.id} = ?", result)
        self._connection.commit()

    def add_transition(self, user_id: int, value: int, comment: str, classification: str):
        self._cursor.execute(f"SELECT MAX(id) FROM {container.TableName.bank}")
        max_id = self._cursor.fetchone()[0]
        new_id = 1 if max_id is None else max_id + 1
        name = self.get_user_status(user_id)[container.ColumnName.name]
        date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        result = new_id, value, comment, name, classification, date,
        self._cursor.execute(f"INSERT OR IGNORE INTO {container.TableName.bank} VALUES (?,?,?,?,?,?)", result)
        self._connection.commit()

    def get_current_balance(self):
        self._cursor.execute(f'SELECT SUM({container.ColumnName.value}) FROM {container.TableName.bank};')
        current_balance = self._cursor.fetchone()[0]
        return current_balance

    def delete_transition(self, transition_id: int):
        query = f"DELETE FROM {container.TableName.bank} WHERE {container.ColumnName.id} = {transition_id}"
        self._cursor.execute(query)
        self._connection.commit()

    def get_transitions_count(self, count=10):
        self._cursor.execute(f"SELECT * FROM {container.TableName.bank} "
                             f"ORDER BY {container.ColumnName.id} DESC LIMIT {count}")
        rows = self._cursor.fetchall()
        text = [f"Баланс: {self.get_current_balance()}"]
        number_count = 0
        for element in rows:
            number_count += 1
            text.append(f"{number_count}.  {element[1]},  {element[2]},  {element[3]},  {element[4]}, {element[5]} ")
        return "\n".join(text)

    def get_month_statistic(self, user_id: int):
        pass

    def get_year_statistic(self, user_id: int):
        pass


class Sql:

    @staticmethod
    def get_month_statistic(user_id: int):
        _sqlClass = SqlOperation()
        statistic = _sqlClass.get_month_statistic(user_id=user_id)
        _sqlClass.close()
        return statistic

    @staticmethod
    def get_year_statistic(user_id: int):
        _sqlClass = SqlOperation()
        statistic = _sqlClass.get_year_statistic(user_id=user_id)
        _sqlClass.close()
        return statistic


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
