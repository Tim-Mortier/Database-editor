def error_message_table(tables):
	return f"usage: <command> <table>\nfor more info type \"help\"\ntables: {tables}"

def error_message_type():
	return "please enter a value with a type corresponding to its header type"

def error_message(table, item):
	return f"please enter a(n) {item} that exists in {table}\nto see records, write: see {table}"

