import sqlite3
from os import path
from settings import DATABASE_PATH


def get_connection():
	return sqlite3.connect(DATABASE_PATH)


def execute_query(query):
	dbconnection = get_connection()
	cursor = dbconnection.cursor()
	return dbconnection, cursor.execute(query)


def commit_query(tuple):
	tuple[0].commit()



