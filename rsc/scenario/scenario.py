
from rsc.const import Const
from tools.sqlOper import Sql


class Scenario:
    const = Const()
    value = const.ColumnName.value
    comment = const.ColumnName.comment
    sql = Sql

    @staticmethod
    def check_in_list_word(text: str, list_word: list):
        return text.rstrip().lstrip().lower() in list_word

    @staticmethod
    def reset_user_status(user_id: int):
        Sql.set_user_status(user_id, Scenario.const.ClassName.choice)


    @staticmethod
    def set_user_status(user_id: int, scenario: str):
        Sql.set_user_status(user_id=user_id, scenario=scenario)
