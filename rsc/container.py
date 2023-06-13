

class Container:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = Settings()
        return cls.instance


class ConstColumnName:
    id = "id"
    value = "value"
    comment = "comment"
    date = "date"
    name = "name"
    scenario = "scenario"
    classification = "classification"


class ConstTableName:
    user = "user"
    bank = "bank"
    cash = "cash"


class ConstKeyName:
    text = "text"
    balance = "balance"
    transition = "transition"


class ConstClassName:
    addTransition = "addTransition"
    first = "first"
    choice = "choice"
    classification = "classification"


class SettingConfig:
    default_scenario = ConstClassName.first


class Settings:
    TableName = ConstTableName
    ColumnName = ConstColumnName
    KeyName = ConstKeyName
    ClassName = ConstClassName
    Config = SettingConfig
