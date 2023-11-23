def error_message_table(tables):
	return f"usage: <command> <table>\nfor more info type \"help\"\ntables: {tables}"

def error_message_record(table):
	return f"please enter an id that exists in {table}\nto see records, write: see {table}"