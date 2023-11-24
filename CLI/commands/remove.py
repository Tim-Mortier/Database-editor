from db.commands_db import select_table, remove
from cli.help_commands import choose_id

def run(command_list):
	table = select_table(command_list)
	if table is not None:
		id = choose_id()
		remove(table, id)

def help():
	return "Removes a record from its table"

def detailed_help():
	return f"\t{help()}\n\tUsage: remove <table>\n\tWhen executing more input will be required of the record's id"