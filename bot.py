from func import entered_command


def main():

    while True:
        command = input("Enter command: ")
        output = entered_command(command)
        if not type(output) == type(list()): # з усіх функцій список повертається тільки з однієї.
            print(output)
        else:
            for contact in output:
                print(contact) 
       
        if output == "Good bye!":
            break
        

if __name__ == "__main__":
    exit(main())