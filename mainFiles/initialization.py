
from data.apiConfig import USER_LIST
from tools.sqlOper import Sql
from rsc.container import Container

sql = Sql()

for user in USER_LIST:
    sql.add_user(user[Container().ColumnName.id], user[Container().ColumnName.name])
