def error_message_table(tables):
	return f"\tusage: <command> <table>\n\tfor more info type <help>\n\ttables: {tables}"

def error_message_type():
	return "\tplease enter a value with a type corresponding to its header type"

def error_message(table, item):
	return f"\tplease enter a(n) {item} that exists in {table}\n\tto see records, write: see {table}"

