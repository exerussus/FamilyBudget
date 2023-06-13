
from mainFiles.familyBudget import FamilyBudget
from data.apiConfig import TELEGRAM_TOKEN
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
                btn1 = types.KeyboardButton("Еда")
                btn2 = types.KeyboardButton("Ремонт")
                btn3 = types.KeyboardButton("Одежда")
                btn4 = types.KeyboardButton("Машина")
                btn5 = types.KeyboardButton("Квартира")
                btn6 = types.KeyboardButton("ХОЗ")
                btn7 = types.KeyboardButton("Другое")
                markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
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
