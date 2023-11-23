from db.commands_db import select_table, get_headers_to_add, insert, check_type
from db.error_messages import error_message_type

def run(command_list):
	table = select_table(command_list)
	if table is not None:
		data = choose_data(table)
		insert(table, data)


def choose_data(table):
	headers = get_headers_to_add(table)
	data = list()
	for header in headers:
		value = input(f"choose {header}: ")
		try: 
			check_type(table, header, value)
			if type(value) == str:
				value = f"\'{value}\'"
			data.append(value)
		except:
			print(error_message_type())
	return data

def help():
	return "Adds a new record to its table"
