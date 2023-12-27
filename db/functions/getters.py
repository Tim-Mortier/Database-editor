from db.functions.sqllite_functions import execute_query, get_connection
from error_messages import InvalidTableCommandError
import pandas as pd


def get_data_from_query(query):
	dbconnection, result = execute_query(query)
	return result.fetchall()


def get_headers_from_query(query):
	dbconnection, cursor = execute_query(query)
	headers = [header[0] for header in cursor.description]
	return headers


def get_values_from_data(data, place):
	return [row[place] for row in data]


def get_tables():
	query = "SELECT name FROM sqlite_master WHERE type='table'"
	result = get_data_from_query(query)
	return get_values_from_data(result, place=0)


def get_table(command_list):
	if len(command_list) != 2:
		raise InvalidTableCommandError(get_string(get_tables()))
	else:
		tables = get_tables()
		table = command_list[1]

		if table in tables:
			return table
		else:
			raise InvalidTableCommandError(get_string(get_tables()))


def get_table_values(table):
	query = f"""
	SELECT *
	FROM {table}
	"""
	return get_data_from_query(query)


def get_header_data(table, with_pk=True):
	query = f"""
	PRAGMA table_info({table})
	"""

	data = get_data_from_query(query)
	if with_pk:
		return data
	else:
		return [row for row in data if not row[5]]


def get_record_data(table, id):
	query= f"""
	SELECT *
	FROM {table}
	WHERE {get_primary_key(table)}={id}
	"""
	return get_data_from_query(query)[0]


def get_headers(table, with_pk=True):
	data = get_header_data(table, with_pk)
	return get_values_from_data(data, place=1)


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
	data = get_data_from_query(query)
	return get_values_from_data(data, place=0)


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
			headers = get_headers_from_query(query)
			data.insert(0, headers)
			return data


def get_foreign_keys(table):
	query = f"PRAGMA foreign_key_list({table})"
	foreign_keys = get_data_from_query(query)
	return foreign_keys


def get_string(data, sep=", "):
	result = ""
	for row in data:
		result += f"{row}{sep}"
	return result[:-len(sep)]


def get_data_query(table):
	query = f"""
	SELECT *
	FROM {table}
	"""
	return query


def get_pandas_table(query):
	conn = get_connection()
	return pd.read_sql(query, conn)
