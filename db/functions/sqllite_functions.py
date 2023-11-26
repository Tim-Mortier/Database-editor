import sqlite3
from os import path

def execute_query(query):
	dbconnection = sqlite3.connect(f"{path.dirname(path.dirname(__file__))}\\expenses.db")
	cursor = dbconnection.cursor()
	return dbconnection, cursor.execute(query)

def commit_query(tuple):
	tuple[0].commit()



