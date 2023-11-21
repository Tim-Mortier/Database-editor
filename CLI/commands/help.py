import importlib

def run():
	commands = importlib.import_module(f'cli.main').get_commands()
	print("commands:")
	print()
	for command in commands:
		message = commands[command].help()
		if message != None:
			print(f"{command}: {message}")

def help():
	pass