
from rsc.container import Container

container = Container()
first_words = [
    "/money"
]

choice_words = {

    container.KeyName.balance: [
        "баланс", "1"
    ],
    container.KeyName.transition: [
        "изменить", "транзакция", "изменение", "добавить", "2"
    ],
    container.KeyName.statisticMonth: [
        "месяц", "за месяц", "1"
    ],
    container.KeyName.statisticYear: [
        "год", "за год", "2"
    ],

}

