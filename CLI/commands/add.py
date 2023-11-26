from cli.functions import check_type
from db.functions.getters import get_headers_without_pk, get_table
from db.functions.table_updates import insert
from db.error_messages import error_message_type

def run(command_list):
	table = get_table(command_list)
	if table is not None:
		data = choose_data(table)
		insert(table, data)


def choose_data(table):
	headers = get_headers_without_pk(table)
	data = list()
	for header in headers:
		while True:
			value = input(f"choose {header}: ")
			try: 
				check_type(table, header, value)
				if type(value) == str:
					value = f"\'{value}\'"
				data.append(value)
				break
			except:
				print(error_message_type())
	return data

def help():
	return "Adds a new record to its table"

def detailed_help():
	return f"\t{help()}\n\tUsage: add <table>"
