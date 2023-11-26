from db.functions.getters import get_headers_without_pk, get_string, get_primary_key, get_primary_key_values
from db.functions.sqllite_functions import execute_query, commit_query


def insert(table, data):
	headers_without_pk = get_headers_without_pk(table)

	query = f"""
	INSERT INTO {table}({get_string(headers_without_pk, ", ")[:-1]})
	values({get_string(data, ", ")[:-1]})
	"""

	commit_query(execute_query(query))

def remove(table, id):
	query = f"""
	DELETE FROM {table} WHERE {get_primary_key(table)}={id}
	"""

	commit_query(execute_query(query))

def update(table, id, header, value):
	if type(value) == str:
		value = f"\"{value}\""
	query= f"""
	UPDATE {table} set {header} = {value}
	WHERE {get_primary_key(table)} == {id}
	"""

	commit_query(execute_query(query))


