

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
    statisticMonth = "statisticMonth"
    statisticYear = "statisticYear"


class ConstScenarioName:
    addTransition = "addTransition"
    first = "first"
    choice = "choice"
    classification = "classification"
    statistic = "statistic"
    statisticChoice = "statisticChoice"


class SettingConfig:
    default_scenario = ConstScenarioName.first


class Settings:
    TableName = ConstTableName
    ColumnName = ConstColumnName
    KeyName = ConstKeyName
    ScenarioName = ConstScenarioName
    Config = SettingConfig

