from typing import Type
from tools.sqlOper import SqlOperation
from rsc.container import Container
from rsc.scenario.first import First
from rsc.scenario.addTrinsition import AddTransition
from rsc.scenario.choice import Choice
from rsc.scenario.classification import Classification


class FamilyBudget:

    def _get_correct_scenario(self, user_id: int) -> Type[First | Choice | AddTransition]:
        user_status = SqlOperation().get_user_status(user_id)
        SqlOperation().close()
        actually_scenario = user_status[Container().ColumnName.scenario]

        match actually_scenario:
            case AddTransition.name:
                scenario_class = AddTransition
            case Choice.name:
                scenario_class = Choice
            case Classification.name:
                scenario_class = Classification
            case _:
                if Container().Config.default_scenario == Container().ClassName.first:
                    scenario_class = First
                else:
                    scenario_class = Choice

        return scenario_class

    def run(self, user_id: int, text: str) -> str:
        try:
            scenario_class = self._get_correct_scenario(user_id)
        except TypeError:
            return "Пользователь не зарегистрирован."
        answer = scenario_class.run(user_id=user_id, text=text)
        return answer
