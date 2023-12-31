class InvalidTableCommandError(Exception):
	def __init__(self, tables):
		message = f"\tusage: <command> <table>\n\tfor more info type <help>\n\ttables: {tables}"
		super().__init__(message)


def error_message(table, item):
	return f"\tplease enter a(n) {item} that exists in {table}\n\tto see records, write: see {table}"


class TableValueNotFoundError(Exception):
	def __init__(self, item, table):
		message = f"\tplease enter a(n) {item} that exists in {table}\n\tto see records, write: see {table}"
		super().__init__(message)

