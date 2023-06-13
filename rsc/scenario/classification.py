
from rsc.scenario.scenario import Scenario


class Classification(Scenario):
    name = Scenario.const.ClassName.classification

    @staticmethod
    def run(user_id: int, text: str) -> str:

        value, comment = Classification.sql.load_cash(user_id=user_id)
        Classification.sql.add_transition(user_id, value, comment, text)
        Classification.reset_user_status(user_id)
        return f"{Classification.sql.get_transitions_count()}"


