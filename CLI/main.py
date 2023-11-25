import importlib
import os
import sys
from cli.help_commands import get_commands

def main():
	commands = get_commands()
		
	while True:
		command = input("command: ")
		command_list = command.split()

		if command_list[0] == "exit":	
			print("exiting...")
			break
		elif command_list[0] not in commands.keys():
			print("\tfor more info type <help>")
		else:
			commands[command_list[0]].run(command_list)

def print_commands(commands_list):
	result = ""
	for command in commands_list:
		result += f"{command} "
	result += "exit"
	return result


