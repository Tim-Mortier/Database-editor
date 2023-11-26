import sqlite3
from db.functions.sqllite_functions import execute_query
from db.error_messages import error_message_table


#get_info
def get_data_from_query(query):
	dbconnection, result = execute_query(query)
	return result.fetchall()
#get_values_from_info
def get_values_from_data(data):
	values = list()
	for row in data:
		values.append(row[1])
	return values

def get_tables():
	query = "SELECT name FROM sqlite_master WHERE type='table';"
	result = get_data_from_query(query)

	tables = set()
	for table in result:
		tables.add(table[0])

	return tables

#select_table
def get_table(command_list):
	if len(command_list) != 2:
		print(error_message_table(get_string(get_tables())))
	else:
		tables = get_tables()
		table = command_list[1]

		if table in tables:
			return table
		else:
			print(error_message_table(get_string(get_tables())))

#get_data
def get_table_values(table):
	query = f"""
	SELECT *
	FROM {table}
	"""
	return get_data_from_query(query)

#get_header_info
def get_header_data(table):
	query = f"""
	PRAGMA table_info({table})
	"""
	return get_data_from_query(query)

def get_record_data(table, id):
	query= f"""
	SELECT *
	FROM {table}
	WHERE {get_primary_key(table)}={id}
	"""
	return get_data_from_query(query)[0]

#get_header_info_to_add
def get_header_data_without_pk(table):
	data = get_header_data(table)
	data_withouth_pk = list()
	for row in data:
		if not row[5]:
			data_withouth_pk.append(row)
	return data_withouth_pk

def get_headers(table):
	data = get_header_data(table)
	return get_values_from_data(data)

#get_headers_to_add
def get_headers_without_pk(table):
	info = get_header_data_without_pk(table)
	return get_values_from_data(info)

def get_primary_key(table):
    query = f"PRAGMA table_info({table})"
    table_info = get_data_from_query(query)

    for column in table_info:
        if column[5]:
            return column[1]

def get_primary_key_values(table):
	primary_key = get_primary_key(table)

	query = f"""
	SELECT {primary_key}
	FROM {table}
	"""

	info = get_data_from_query(query)
	values = list()
	for row in info:
		values.append(row[0])
	return values

def get_joined_table_data():
	tables = get_tables()
	for table in tables:
		foreign_keys = get_foreign_keys(table)
		if len(foreign_keys) != 0:
			query=f"""
			SELECT *
			FROM {table}
			"""
			for row in foreign_keys:
				join_table = row[2]
				fk_join_table = row[4]
				fk_old_table = row[3]
				query +=f"INNER JOIN {join_table} ON {table}.{fk_old_table}={join_table}.{fk_join_table}"
			data = get_data_from_query(query)
			dbconnection, cursor = execute_query(query)
			headers = list()
			for header in cursor.description:
				headers.append(header[0])
			data.insert(0, tuple(headers))
			return data

def get_foreign_keys(table):
	query = f"PRAGMA foreign_key_list({table})"
	foreign_keys = get_data_from_query(query)
	return foreign_keys

def get_string(data, sep=" "):
	result = ""
	for row in data:
		result += f"{row}{sep}"
	return result.strip()