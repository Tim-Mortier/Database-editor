from db.commands_db import select_table, get_header_info_to_add, translate, remove


def run(command_list):
	table = select_table(command_list)
	if table is not None:
		id = choose_id()
		remove(table, id)

def choose_id():
	while True:
		id = input("choose id: ")
		try:
			return int(id)
		except:
			print("Please choose a number")


def help():
	return "Removes a record from its table"