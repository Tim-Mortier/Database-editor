from commands import *
import os

command_prefixes = set()

with os.scandir('commands') as entries:
	for entry in entries:
		command_prefixes.add(entry.name.strip(".py"))
		
while True:
	command = input("command: ")
	command_list = command.split()

	if command_list[0] not in command_prefixes:
		print("Usage: <command> <option>")
		print(f"Commands: {command_prefixes}")
	else:
		print(command)
		commands.test()
		break	


