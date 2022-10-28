from main_logic import entered_command


def main():

    while True:
        command = input("Enter command: ")
        output = entered_command(command)
        if type(output) == type(list()): # з усіх функцій список повертається тільки з однієї.
            for contact in output:
                print(contact)
        else:
            print(output) 
       
        
        if output == "Good bye!":
            break
        

if __name__ == "__main__":
    exit(main())