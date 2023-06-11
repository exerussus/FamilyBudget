
from main.familyBudget import FamilyBudget
from data.apiConfig import TELEGRAM_TOKEN
import telebot
from telebot import types


class TeleBot:

    def __init__(self):
        self._familyBudget = FamilyBudget()
        self._bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode=None)

    def run(self):
        @self._bot.message_handler(content_types=['text'])
        def get_message(message):
            user_id = message.from_user.id
            text = message.text
            answer = self._familyBudget.run(user_id=user_id, text=text)
            if answer is None:
                self._bot.send_message(message.from_user.id, "Команда не распознана.")
            elif answer == "Выберите действие: \n1. Баланс\n2. Добавить транзакцию":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                btn1 = types.KeyboardButton("Баланс")
                btn2 = types.KeyboardButton("Транзакция")
                markup.add(btn1, btn2)
                self._bot.send_message(message.from_user.id, answer, reply_markup=markup)
            else:
                self._bot.send_message(message.from_user.id, answer, reply_markup=types.ReplyKeyboardRemove())
        self._bot.polling(none_stop=True, interval=1)


if __name__ == "__main__":
    _telebot = TeleBot()
    _telebot.run()
