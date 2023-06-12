
from data.apiConfig import USER_LIST
from tools.sqlOper import Sql
from rsc.const import Const

sql = Sql()

for user in USER_LIST:
    sql.add_user(user[Const().ColumnName.id], user[Const().ColumnName.name])
