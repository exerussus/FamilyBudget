from data.wordsConfig import first_words
from rsc.scenario.scenario import Scenario


class First(Scenario):
    name = Scenario.const.ClassName.first

    @staticmethod
    def run(user_id: int, text: str) -> str:
        if First.check_in_list_word(text, first_words):
            First.set_user_status(user_id, First.const.ClassName.choice)
            return "Выберите действие: \n1. Баланс\n2. Добавить транзакцию"
