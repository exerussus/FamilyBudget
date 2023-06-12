from typing import Type

from tools.sqlOper import SqlOperation
from rsc.const import Const
from rsc.scenario.first import First
from rsc.scenario.addTrinsition import AddTransition
from rsc.scenario.choice import Choice


class FamilyBudget:

    def _get_correct_scenario(self, user_id: int) -> Type[First | Choice | AddTransition]:
        user_status = SqlOperation().get_user_status(user_id)
        SqlOperation().close()
        actually_scenario = user_status[Const().ColumnName.scenario]

        match actually_scenario:
            case AddTransition.name:
                scenario_class = AddTransition
            case Choice.name:
                scenario_class = Choice
            case _:
                scenario_class = First

        return scenario_class

    def run(self, user_id: int, text: str) -> str:
        scenario_class = self._get_correct_scenario(user_id)
        answer = scenario_class.run(user_id=user_id, text=text)
        return answer
