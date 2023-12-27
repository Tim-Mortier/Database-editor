import os
import sys
import importlib
from db.functions.getters import get_header_data


def choose_id():
	while True:
		id = input("choose id: ")
		try:
			return int(id)
		except:
			print("Please choose a number")


def get_commands():
	file_dir = os.path.dirname(__file__)
	sys.path.append(os.path.dirname(file_dir))
	command_dir = os.path.join(file_dir, 'commands')
	command_files = [f[:-3] for f in os.listdir(command_dir) if f.endswith('.py')]
	
	commands = dict()
	for command in command_files:
		module = importlib.import_module(f'cli.commands.{command}')
		commands[command] = module
	return commands


def check_type(table, header, value):
	header_info = get_header_data(table)
	for row in header_info:
		name = row[1]
		if name == header:
			sql_type = row[2]
			if sql_type == "INTEGER":
				int(value)
			elif sql_type == "NUMERIC":
				float(value)