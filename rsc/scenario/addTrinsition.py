
from rsc.scenario.scenario import Scenario


class AddTransition(Scenario):
    name = Scenario.container.ClassName.addTransition

    @staticmethod
    def _try_calc(text: str) -> str:

        try:
            return eval(text)
        except:
            return text

    @staticmethod
    def _parse_transition(text: str) -> dict:
        split_text = text.split(",")
        value = split_text[0].lstrip().rstrip()
        comment = split_text[1].lstrip().rstrip()
        value = AddTransition._try_calc(value)

        try:
            value = int(value)
        except:
            value = 0
            comment = "Ошибка ввода данных."
        returned_info = {AddTransition.value: value,
                         AddTransition.comment: comment}
        return returned_info

    @staticmethod
    def run(user_id: int, text: str) -> str:
        try:
            info_dict = AddTransition._parse_transition(text)
            value, comment = info_dict[AddTransition.value], info_dict[AddTransition.comment]

            if value != 0:
                if value < 0:
                    AddTransition.sql.save_cash(user_id, value, comment)
                    AddTransition.set_user_status(user_id, AddTransition.container.ClassName.classification)
                    return "Введите категорию: "
                else:
                    AddTransition.sql.add_transition(user_id=user_id, value=value, comment=comment, classification="+")
                    AddTransition.reset_user_status(user_id)
                    return f"{AddTransition.sql.get_transitions_count()}"
            else:
                return comment
        except:
            AddTransition.reset_user_status(user_id)
            return "Ошибка ввода данных."

