from db.functions.getters import get_table, get_data_query, get_pandas_table


def run(command_list):
	table = get_table(command_list)
	if table is not None:
		print(get_pandas_table(get_data_query(table)))


def help():
	return "Shows a table of the database"


def detailed_help():
	return f"\t{help()}\n\tUsage: see <table>"