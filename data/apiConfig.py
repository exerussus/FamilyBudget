
from data.private.privateConfig import TELEGRAM_TOKEN as TOKEN
from data.private.privateConfig import USER_LIST as _USER_LIST
from data.private.privateConfig import CLASSIFICATION_LIST as _CLASSIFICATION_LIST


user_id = "id"
user_name = "name"


INPUT_FUNCTION = input
OUTPUT_FUNCTION = print

TELEGRAM_TOKEN = TOKEN
USER_LIST: dict[user_id: int, user_name: str] = _USER_LIST
CLASSIFICATION_LIST: list[str] = _CLASSIFICATION_LIST
