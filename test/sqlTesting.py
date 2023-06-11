from tools.sqlOper import SqlOperation

user_id = 1
user_name = "Илья"
transition_value = 100
transition_comment = "Нашел на улице"

sql = SqlOperation()
sql.add_user(user_id, user_name)
print(sql.get_user_status(user_id))
sql.add_transition(user_id, transition_value, transition_comment)
sql.add_transition(user_id, transition_value, transition_comment)
sql.add_transition(user_id, transition_value, transition_comment)
print(sql.get_current_balance())
print(sql.get_transitions_count())
print(sql.get_user_status(user_id))
