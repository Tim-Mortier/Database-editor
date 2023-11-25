from db.commands_db import return_string

class Record():
	def __init__(self, headers, data):
		self.__headers = headers 
		self.__data = data

	def get_headers(self):
		return self.__headers

	def __str__(self):
		return f"\t{return_string(self.__headers)}\n\t{return_string(self.__data)}"





