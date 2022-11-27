from main_logic import entered_command
from output_logic import output_logic


def main():

    while True:
        command = input("Enter command: ")
        output = entered_command(command)
        output = output_logic(text=output[0],type_str=output[1])
        print(output)

        if output == "Good bye!":
            break


if __name__ == "__main__":
    exit(main())