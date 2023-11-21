import sqlite3
import os

def run(command_list):
	option = command_list[1]
	options = get_options()

	if option in options:
		print_table(command_list, option)
	else:
		print_options(options)
	
	
def get_info(query):
	dbconnection = sqlite3.connect(f"{os.path.dirname(__file__)[:-12]}db\\expenses.db")
	cursor = dbconnection.cursor()

	result = cursor.execute(query)
	return cursor.fetchall()

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

def get_options():
	query = "SELECT name FROM sqlite_master WHERE type='table';"
	result = get_info(query)

	options = set()
	for option in result:
		options.add(option[0])

	return options

def print_table(command_list, table):
	headers = get_headers(table)
	result = ""
	for header in headers:
		result += str(header[1]) + " "
	print(result.strip())
	
	data = get_data(table)
	for row in data:
		result = ""
		for i in range(len(row)):
			result += str(row[i]) + " "
		print(result.strip())

def print_options(options):
	result = ""
	for option in options:
		result += str(option) + " "
	print(f"options: {result}")





def help():
	return "Shows your expenses or its categories"