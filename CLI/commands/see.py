from db.functions.getters import get_table_values, get_headers, get_table, get_string_table

def run(command_list):
	table = get_table(command_list)
	if table is not None:
		print_table(table)

def print_table(table):
	headers = get_headers(table)
	print(f"\t{get_string_table(headers):<10}")
	
	data = get_table_values(table)
	for row in data:
		result = ""
		for i in range(len(row)):
			result += f"{row[i]:<15}"
		print(f"\t{result.strip()}")

def help():
	return "Shows a table of the database"

def detailed_help():
	return f"\t{help()}\n\tUsage: see <table>"