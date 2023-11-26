from db.functions.table_updates import remove
from db.functions.getters import get_table
from cli.functions import choose_id

def run(command_list):
	table = get_table(command_list)
	if table is not None:
		id = choose_id()
		remove(table, id)

def help():
	return "Removes a record from its table"

def detailed_help():
	return f"\t{help()}\n\tUsage: remove <table>\n\tWhen executing more input will be required of the record's id"