import sqlite3
import os

def get_info(query):
	dbconnection = sqlite3.connect(f"{os.path.dirname(__file__)[:-3]}\\db\\expenses.db")
	cursor = dbconnection.cursor()

	result = cursor.execute(query).fetchall()
	return result

def get_column_names():
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

def get_headers(table):
	query = f"""
	PRAGMA table_info({table})
	"""
	return get_info(query)