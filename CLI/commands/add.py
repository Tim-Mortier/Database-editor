from db.commands_db import get_tables, get_data, get_headers, return_string


def run(command_list):
	get_record_info()


def get_record_info():
	table = choose_table()

	headers = get_headers(table)
	print(headers)
	for header in headers:
		value = input(f"choose {header}: ")
		print(type(value))
	print(get_headers("expenses"))
	#table = input("table: ")

def choose_table():
	tables = get_tables()
	while True:	
		table = input("choose table: ")
		if table not in tables:
			print(f"choose out of these tables: {return_string()}")
		else:
			return table


def get_error_message():
	print(f"usage: <command> <option> <name>\nfor more info type \"help\"")

def help():
	return "Adds a new record to it's table"
