from cli.cli_functions import get_commands


def run(command_list):
	commands = get_commands()
	if len(command_list) == 1:
		print("commands:")
		for command in commands:
			message = commands[command].help()
			if message is not None:
				print(f"\t{command}: {message}")
		print("\texit: Closes the program")
		print("\n\tfor more info about a command, write: help <command>")
	else:
		try:
			message = commands[command_list[1]].detailed_help()
			print(message)
		except KeyError:
			print("\tCommand doesn't exist. Write <help> to see all commands")


def help():
	pass


def detailed_help():
	pass