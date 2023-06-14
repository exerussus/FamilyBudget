import os


def run():

    install = '1'
    init = '2'
    uninstall = '3'
    escape = '0'


    def get_choice():
        _choice = input("1. Установить приватные конфиги (data/private/privateConfig.py)\n"
                       "2. Проинициализировать настроенные конфиги\n"
                       "3. Удалить все настройки, конфиги и базу данных\n"
                       "0. Выйти\n"
                        "Ввод (1\\2\\3\\0): ")

        if _choice == escape:
            exit(0)
        else:
            if _choice not in [install, init, uninstall]:
                return get_choice()
            else:
                return _choice


    choice = get_choice()

    if choice == install:
        if not os.path.exists("data/private"):
            os.makedirs("data/private")
        with open("data/private/privateConfig.py", "w") as f:
            f.write("FIRST = {'id': 0, 'name': ''}\n")
            f.write("SECOND = {'id': 0, 'name': ''}\n")
            f.write("TELEGRAM_TOKEN = ''\n")
            f.write("USER_LIST = [FIRST, SECOND]")
            f.write('CLASSIFICATION_LIST = ["Еда", "Машина", "Ремонт", '
                    '"Одежда", "Квартира", "ХОЗЫ", "Другое"]')

    elif choice == init:

        from data.apiConfig import USER_LIST
        from tools.sqlOper import Sql
        from rsc.container import Container

        sql = Sql()
        for user in USER_LIST:
            sql.add_user(user[Container().ColumnName.id], user[Container().ColumnName.name])

    elif choice == uninstall:
        if os.path.exists("data/private/privateConfig.py"):
            os.remove("data/private/privateConfig.py")
        if os.path.exists("data/database.db"):
            os.remove("data/database.db")

    else:
        input("Непредвиденная ошибка...")
