from db.commands_db import select_table, get_header_info_to_add, insert


def run(command_list):
	table = select_table(command_list)
	if table is not None:
		data = choose_data(table)
		insert(table, data)


def choose_data(table):
	header_info = get_header_info_to_add(table)
	data = list()
	for info in header_info:
		while True: 
			value = input(f"choose {info[1]}: ")
			sql_type = info[2]
			try: 
				if sql_type == "INTEGER":
					data.append(int(value))
					break
				elif sql_type == "NUMERIC":
					data.append(float(value))
					break
				elif sql_type == "TEXT":
					data.append(f"\'{value}\'")
					break
			except:
				print(f"enter of type {sql_type}")
	return data

def help():
	return "Adds a new record to its table"
