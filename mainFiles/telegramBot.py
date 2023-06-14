
from mainFiles.familyBudget import FamilyBudget
from data.apiConfig import TELEGRAM_TOKEN, CLASSIFICATION_LIST
import telebot
from telebot import types
from tools.debug import log
from rsc.container import Container


class TeleBot:

    def __init__(self, debug_mode=False):
        self._familyBudget = FamilyBudget()
        self._bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode=None)
        self.debug_mode = debug_mode
        Container().Config.default_scenario = Container().ClassName.choice

    def log(self, text: str):
        log(text=text, debug_mode=self.debug_mode)

    def run(self):
        @self._bot.message_handler(content_types=['text'])
        def get_message(message):
            user_id = message.from_user.id
            text = message.text
            self.log(f"{user_id}: {text}")
            answer = self._familyBudget.run(user_id=user_id, text=text)
            if answer is None:
                self.log(f"{user_id}: Команда не распознана...")
                self._bot.send_message(message.from_user.id, "Команда не распознана.")
            elif answer == "Введите категорию: ":
                self.log(f"{user_id}: Ожидание выбора категории...")
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

                button_list = []
                for classification in CLASSIFICATION_LIST:
                    button_list.append(types.KeyboardButton(classification))
                button_tuple = tuple(button_list)
                markup.add(*button_tuple)
                self._bot.send_message(message.from_user.id, answer, reply_markup=markup)
            elif "Введите транзакцию" in answer:
                self.log(f"{user_id}: Ожидание ввода транзакции...")
                self._bot.send_message(message.from_user.id, answer, reply_markup=types.ReplyKeyboardRemove())
            else:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                btn1 = types.KeyboardButton("Баланс")
                btn2 = types.KeyboardButton("Транзакция")
                markup.add(btn1, btn2)
                self._bot.send_message(message.from_user.id, answer, reply_markup=markup)
        self._bot.polling(none_stop=True, interval=1)


if __name__ == "__main__":
    _telebot = TeleBot(debug_mode=True)
    _telebot.run()
