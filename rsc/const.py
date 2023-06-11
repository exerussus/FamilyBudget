

class Const:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = Constant()
        return cls.instance


class ConstColumnName:
    id = "id"
    value = "value"
    comment = "comment"
    date = "date"
    name = "name"
    scenario = "scenario"


class ConstTableName:
    user = "user"
    bank = "bank"


class ConstKeyName:
    text = "text"
    balance = "balance"
    transition = "transition"


class ConstClassName:
    addTransition = "addTransition"
    first = "first"
    choice = "choice"


class Constant:
    TableName = ConstTableName
    ColumnName = ConstColumnName
    KeyName = ConstKeyName
    ClassName = ConstClassName
