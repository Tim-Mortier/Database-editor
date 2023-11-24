from cli.help_commands import choose_id
from db.commands_db import select_table, get_primary_key_values, get_record, get_headers, return_string, check_type, update
from db.error_messages import error_message, error_message_type

def run(command_list):
	table = select_table(command_list)
	if table is not None:
		id = choose_id()
		if id not in get_primary_key_values(table):
			print(error_message(table, "record"))
		else:
			record = get_record(table, id)
			headers = get_headers(table)
			print("record:")
			print(return_string(headers))
			print(return_string(record))
			header = input("choose one header to change: ")
			if header not in headers:
				print(error_message(table, "header"))
			else:
				value = input("enter new value: ")
				try:
					check_type(table, header, value)
					update(table, id, header, value)
				except:
					print(error_message_type())


def help():
	return "Change a record in its table"

def detailed_help():
	return f"\t{help()}\n\tUsage: remove <table>\n\tWhen executing more input will be required of the record's id"