import csv
from db.commands_db import join_all_tables
def run(command_list):
	#name = input("Name of the created file: ")
	join_all_tables()
	#with open(f"{name}.csv", 'x', newline='') as file:
	#	writer = csv.writer(file, delimiter=";")

def help():
	return "Exports the database to a new csv file"