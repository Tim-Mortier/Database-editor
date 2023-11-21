import importlib
import os
import sys

def main():
	commands = get_commands()
		
	while True:
		command = input("command: ")
		command_list = command.split()

		if command_list[0] == "exit":	
			print("exiting...")
			break
		elif command_list[0] not in commands.keys():
			print("usage: <command> <option> <name>")
			print("for more info type \"help\"")
		else:
			commands[command_list[0]].run(command_list)

def print_commands(commands_list):
	result = ""
	for command in commands_list:
		result += f"{command} "
	result += "exit"
	return result

def get_commands():
	file_dir = os.path.dirname(__file__)
	sys.path.append(os.path.dirname(file_dir))
	command_dir = os.path.join(file_dir, 'commands')
	print(command_dir)
	command_files = [f[:-3] for f in os.listdir(command_dir) if f.endswith('.py')]



	commands = dict()
	for command in command_files:
		module = importlib.import_module(f'cli.commands.{command}')
		commands[command] = module
	return commands


if __name__ == "__main__":
	main()


