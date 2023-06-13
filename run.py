from mainFiles.telegramBot import TeleBot


if __name__ == "__main__":
    _telebot = TeleBot(debug_mode=True)
    _telebot.run()
