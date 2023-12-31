from cli.cli_functions import get_commands
from errors import TableValueNotFoundError, InvalidTableCommandError


def main():
	commands = get_commands()

	while True:
		command = input("command: ")
		command_list = command.split()

		if len(command_list) == 0:
			print("\tfor more info type <help>")
		elif command_list[0] == "exit":
			print("exiting...")
			break
		elif command_list[0] not in commands.keys():
			print("\tfor more info type <help>")
		else:
			try:
				commands[command_list[0]].run(command_list)
			except TableValueNotFoundError as e:
				print(e)
			except InvalidTableCommandError as e:
				print(e)
			except ValueError:
				print("\tplease enter a value with a type corresponding to its header type")
			except TypeError:
				print("\tToo many arguments, for more info type help")


def print_commands(commands_list):
	result = ""
	for command in commands_list:
		result += f"{command} "
	result += "exit"
	return result


if __name__ == "__main__":
	main()
