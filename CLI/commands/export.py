import csv
import os
from db.functions.getters import get_joined_table_data

def run(command_list):
	file_name = input("Name of the created file: ")
	os.chdir(f"{os.getcwd()}\\exports")
	try:
		export_table_data(file_name)
	except Exception as e:
		print(e)
		print("file already exists, please choose another")
	os.chdir("..")
	
def export_table_data(file_name):
	with open(f"{file_name}.csv", 'x', newline='') as file:
		writer = csv.writer(file, delimiter=";")
		for row in get_joined_table_data():
			writer.writerow(row)

def help():
	return "Exports the database to a new csv file"

def detailed_help():
	return f"\t{help()}\n\tUsage: export"