from cli.help_commands import choose_id
from db.commands_db import select_table, change

def run(command_list):
	table = select_table(command_list)
	if table is not None:
		id = choose_id()
		change(table, id)

def help():
	return "Change a record in its table"