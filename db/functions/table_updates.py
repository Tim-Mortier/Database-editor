from db.functions.getters import get_headers, get_string, get_primary_key
from db.functions.sqllite_functions import execute_query, commit_query


def insert(table, data):
	headers = get_headers(table, with_pk=False)

	query = f"""
	INSERT INTO {table}({get_string(headers, ", ")[:-1]})
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


