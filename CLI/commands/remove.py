from db.commands_db import select_table, remove
from cli.help_commands import choose_id

def run(command_list):
	table = select_table(command_list)
	if table is not None:
		id = choose_id()
		remove(table, id)

def help():
	return "Removes a record from its table"