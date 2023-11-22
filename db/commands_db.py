import sqlite3
import os

translator = {"TEXT": str, "NUMERIC": int}

def get_info(query):
	dbconnection = sqlite3.connect(f"{os.path.dirname(__file__)[:-3]}\\db\\expenses.db")
	cursor = dbconnection.cursor()

	result = cursor.execute(query).fetchall()
	return result

def get_tables():
	query = "SELECT name FROM sqlite_master WHERE type='table';"
	result = get_info(query)

	names = set()
	for name in result:
		names.add(name[0])

	return names

def get_data(table):
	query = f"""
	SELECT *
	FROM {table}
	"""
	return get_info(query)

def get_header_info(table):
	query = f"""
	PRAGMA table_info({table})
	"""
	return get_info(query)

def get_headers(table):
	info = get_header_info(table)
	headers = list()
	for row in info:
		headers.append(row[1])
	return headers

def return_string(data):
	result = ""
	for row in data:
		result += f"{row} "
	return result.strip()

def translate(sql_value):
	return translator[sql_value]

def select_table(command_list):
	if len(command_list) != 2:
		print(get_error_message())
	else:
		tables = get_tables()
		table = command_list[1]

		if table in tables:
			return table
		else:
			print(get_error_message())

def get_error_message():
	tables = get_tables()
	return f"usage: <command> <table>\nfor more info type \"help\"\ntables: {return_string(tables)}"