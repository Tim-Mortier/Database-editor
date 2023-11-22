import sqlite3
import os
from db.commands_db import get_tables, get_data, get_headers, return_string, select_table

def run(command_list):
	table = select_table(command_list)
	if table is not None:
		print_table(table)

def print_table(table):
	headers = get_headers(table)
	print(return_string(headers))
	
	data = get_data(table)
	for row in data:
		result = ""
		for i in range(len(row)):
			result += f"{row[i]} "
		print(result.strip())

def get_error_message():
	tables = get_tables()
	return f"usage: <command> <option> <table>\nfor more info type \"help\"\ntables: {return_string(tables)}"


def help():
	return "Shows your expenses or its categories"