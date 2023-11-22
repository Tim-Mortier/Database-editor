import sqlite3
import os

translator = {"TEXT": str, "NUMERIC": float, "INTEGER": int}

def execute_query(query):
	dbconnection = sqlite3.connect(f"{os.path.dirname(__file__)[:-3]}\\db\\expenses.db")
	cursor = dbconnection.cursor()
	return dbconnection, cursor.execute(query)

def get_info(query):
	dbconnection, result = execute_query(query)
	return result.fetchall()

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

def get_header_info_to_add(table):
	info = get_header_info(table)
	new_info = list()
	for row in info:
		if row[5] == 0:
			new_info.append(row)
	return new_info

def get_headers(table):
	info = get_header_info(table)
	headers = list()
	for row in info:
		headers.append(row[1])
	return headers

def get_headers_to_add(table):
	info = get_header_info_to_add(table)
	headers = list()
	for row in info:
		headers.append(row[1])
	return headers

def return_string(data, sep=" "):
	result = ""
	for row in data:
		result += f"{row}{sep}"
	return result.strip()

def translate(sql_type):
	return translator[sql_type]

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

def insert(table, data):
	headers_to_add = get_headers_to_add(table)

	query = f"""
	INSERT INTO {table}({return_string(headers_to_add, ", ")[:-1]})
	values({return_string(data, ", ")[:-1]})
	"""

	print(query)

	dbconnection, result = execute_query(query)
	dbconnection.commit()


def get_error_message():
	tables = get_tables()
	return f"usage: <command> <table>\nfor more info type \"help\"\ntables: {return_string(tables)}"