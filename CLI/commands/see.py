import sqlite3
import os
from db.commands_db import get_column_names, get_data, get_headers

def run(command_list):
	if len(command_list) != 2:
		print(get_error_message())
	else:
		names = get_column_names()
		name = command_list[1]

		if name in names:
			print_table(command_list, name)
		else:
			print(get_error_message())
	

def print_table(command_list, table):
	headers = get_headers(table)
	result = ""
	for header in headers:
		result += f"{header[1]} "
	print(result.strip())
	
	data = get_data(table)
	for row in data:
		result = ""
		for i in range(len(row)):
			result += f"{row[i]} "
		print(result.strip())

def get_string_names(names):
	result = ""
	for name in names:
		result += f"{name} "
	return result


def get_error_message():
	names = get_column_names()
	return f"usage: <command> <option> <name>\nfor more info type \"help\"\nnames: {get_string_names(names)}"


def help():
	return "Shows your expenses or its categories"