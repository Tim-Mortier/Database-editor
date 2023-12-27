from cli.cli_functions import check_type
from db.functions.getters import get_headers, get_table
from db.functions.table_updates import insert


def run(command_list):
	table = get_table(command_list)
	if table is not None:
		data = choose_data(table)
		insert(table, data)


def choose_data(table):
	headers = get_headers(table, with_pk=False)
	data = list()
	for header in headers:
		value = input(f"choose {header}: ")
		check_type(table, header, value)
		if type(value) == str:
			value = f"\'{value}\'"
		data.append(value)

	return data


def help():
	return "Adds a new record to its table"


def detailed_help():
	return f"\t{help()}\n\tUsage: add <table>"
