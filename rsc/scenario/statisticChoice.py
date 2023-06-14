
from data.wordsConfig import choice_words
from rsc.scenario.scenario import Scenario
from random import choice as random_choice


class StatisticChoice(Scenario):
    name = Scenario.container.ScenarioName.statisticChoice

    @staticmethod
    def run(user_id: int, text: str) -> str:
        if StatisticChoice.check_in_list_word(text, choice_words[StatisticChoice.container.KeyName.statisticMonth]):
            StatisticChoice.reset_user_status(user_id)
            return f"{StatisticChoice.sql.get_transitions_count()}"
        elif StatisticChoice.check_in_list_word(text, choice_words[StatisticChoice.container.KeyName.transition]):
            StatisticChoice.set_user_status(user_id, StatisticChoice.container.ScenarioName.addTransition)
            return f"Введите транзакцию, пример"
        else:
            StatisticChoice.reset_user_status(user_id)
            return "Некорректный ввод данных"
