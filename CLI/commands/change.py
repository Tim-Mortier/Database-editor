from cli.functions import choose_id, check_type
from db.functions.getters import get_primary_key_values, get_record_data, get_headers, get_table
from db.functions.table_updates import update
from db.error_messages import error_message, error_message_type
from classes.record import Record

def run(command_list):
	table = get_table(command_list)
	if table is not None:
		id = choose_id()
		if id not in get_primary_key_values(table):
			print(error_message(table, "record"))
		else:
			record = Record(get_headers(table), get_record_data(table, id))

			print(f"\tRecord:\n {record}")
		
			header = input("choose one header to change: ")
			if header not in record.get_headers():
				print(error_message(table, "header"))
			else:
				value = input("enter new value: ")
				try:
					check_type(table, header, value)
					update(table, id, header, value)
				except Exception as e:
					print(e)
					print(error_message_type())

def help():
	return "Change a record in its table"

def detailed_help():
	return f"\t{help()}\n\tUsage: remove <table>\n\tWhen executing more input will be required of the record's id"