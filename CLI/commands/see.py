import sqlite3
import os
from db.functions.getters import get_tables, get_table_values, get_headers, get_table, get_string

def run(command_list):
	table = get_table(command_list)
	if table is not None:
		print_table(table)

def print_table(table):
	headers = get_headers(table)
	print(f"\t{get_string(headers)}")
	
	data = get_table_values(table)
	for row in data:
		result = ""
		for i in range(len(row)):
			result += f"{row[i]} "
		print(f"\t{result.strip()}")

#def get_error_message():
#	tables = get_tables()
#	return f"usage: <command> <option> <table>\nfor more info type \"help\"\ntables: {get_string(tables)}"


def help():
	return "Shows a table of the database"

def detailed_help():
	return f"\t{help()}\n\tUsage: see <table>"