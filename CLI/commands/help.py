import importlib

def run(command_list):
	commands = importlib.import_module(f'cli.main').get_commands()
	print("commands:")
	print()
	for command in commands:
		message = commands[command].help()
		if message != None:
			print(f"{command}: {message}")
	print("exit: Closes the program")

def help():
	pass