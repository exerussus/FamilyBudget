
from data.private.privateConfig import TELEGRAM_TOKEN as TOKEN
from data.private.privateConfig import ILYA_ID, BETH_ID
from rsc.container import Container

user_id = Container().ColumnName.id
user_name = Container().ColumnName.name


INPUT_FUNCTION = input
OUTPUT_FUNCTION = print

TELEGRAM_TOKEN = TOKEN
USER_LIST: dict[user_id: int, user_name: str] = [
    ILYA_ID, BETH_ID
]
