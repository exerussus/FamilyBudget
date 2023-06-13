from data.wordsConfig import choice_words
from rsc.scenario.scenario import Scenario
from random import choice as random_choice


class Choice(Scenario):
    name = Scenario.const.ClassName.choice

    @staticmethod
    def run(user_id: int, text: str) -> str:
        _random_example = ["900, репетиторство",
                           "-350, покупка еды",
                           "-2500, ремонт машины",
                           "500, найдены в кладовой",
                           "-125, мороженое",
                           "2000, подарок от бабушки"]
        if Choice.check_in_list_word(text, choice_words[Choice.const.KeyName.balance]):
            Choice.reset_user_status(user_id)
            return f"{Choice.sql.get_transitions_count()}"
        elif Choice.check_in_list_word(text, choice_words[Choice.const.KeyName.transition]):
            Choice.set_user_status(user_id, Choice.const.ClassName.addTransition)
            return f"Введите транзакцию, пример: {random_choice(_random_example)}"
        else:
            Choice.reset_user_status(user_id)
            return "Некорректный ввод данных"
