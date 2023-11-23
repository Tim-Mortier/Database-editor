import sqlite3
import os
from db.error_messages import error_message_table, error_message_record

def execute_query(query):
	dbconnection = sqlite3.connect(f"{os.path.dirname(__file__)[:-3]}\\db\\expenses.db")
	cursor = dbconnection.cursor()
	return dbconnection, cursor.execute(query)

def commit_query(tupel):
	tupel[0].commit()

def get_values_from_info(info):
	values = list()
	for row in info:
		values.append(row[1])
	return values


def get_info(query):
	dbconnection, result = execute_query(query)
	return result.fetchall()

def get_tables():
	query = "SELECT name FROM sqlite_master WHERE type='table';"
	result = get_info(query)

	tables = set()
	for table in result:
		tables.add(table[0])

	return tables

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
		if not row[5]:
			new_info.append(row)
	return new_info

def get_headers(table):
	info = get_header_info(table)
	return get_values_from_info(info)

def get_headers_to_add(table):
	info = get_header_info_to_add(table)
	return get_values_from_info(info)

def return_string(data, sep=" "):
	result = ""
	for row in data:
		result += f"{row}{sep}"
	return result.strip()

def select_table(command_list):
	if len(command_list) != 2:
		print(error_message_table(return_string(get_tables())))
	else:
		tables = get_tables()
		table = command_list[1]

		if table in tables:
			return table
		else:
			print(error_message_table(return_string(get_tables())))


def get_primary_key(table):
    query = f"PRAGMA table_info({table})"
    table_info = get_info(query)

    for column in table_info:
        if column[5]:
            return column[1]

def get_primary_key_values(table):
	primary_key = get_primary_key(table)

	query = f"""
	SELECT {primary_key}
	FROM {table}
	"""

	info = get_info(query)
	values = list()
	for row in info:
		values.append(row[0])
	return values

def get_foreign_keys(table):
	query = f"PRAGMA foreign_key_list({table})"
	foreign_keys = get_info(query)
	return foreign_keys

def insert(table, data):
	headers_to_add = get_headers_to_add(table)

	query = f"""
	INSERT INTO {table}({return_string(headers_to_add, ", ")[:-1]})
	values({return_string(data, ", ")[:-1]})
	"""

	commit_query(execute_query(query))

def remove(table, id):
	query = f"""
	DELETE FROM {table} WHERE {get_primary_key(table)}={id}
	"""

	commit_query(execute_query(query))

def change(table, id):
	if id not in get_primary_key_values(table):
		print(error_message_record(table))
	else:
		print("succes")

def join_all_tables():
	tables = get_tables()
	for table in tables:
		foreign_keys = get_foreign_keys(table)
		if len(foreign_keys) != 0:
			query=f"""
			SELECT *
			FROM {table}
			"""
			for row in foreign_keys:
				query +=f"INNER JOIN {row[2]} ON {table}.{row[3]}={row[2]}.{row[4]}"
			print(return_string(get_info(query)))

