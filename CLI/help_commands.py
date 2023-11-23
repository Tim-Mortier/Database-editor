def choose_id():
	while True:
		id = input("choose id: ")
		try:
			return int(id)
		except:
			print("Please choose a number")