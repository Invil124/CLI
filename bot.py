
def main():
    CONNTACTS = {}
    
    def error_func(hanndler):

        def wrapper():
            try:
                hanndler()
            except IndexError as error_int:
                print("Give me name and phone please")
            except KeyError as er:
                print("Wrong name try aggain")

        return wrapper


    def greet_func():
        return print("How can I help you?")

    def show_func():
        for name, phone in CONNTACTS.items():
            name = name.title()
            print(f"{name}: {phone}")
        
    @error_func
    def change_func():
        name = input("Enter current name: ")
       
        name = name.strip().lower()
        if not name in CONNTACTS.keys():
            return print("Current name not find.")
        new_phone = input("Enter new phone number: ")
        if not (new_phone.isdigit() and (13 >= len(new_phone) >=9)):
            return print("Invalid phone number.Try again.")    
        CONNTACTS[name] = new_phone
        print("Phone successfully changed")


    @error_func
    def add_func():
        contact = input("Enter name and phone : ")
        contact = contact.strip().split()
        name = contact[0].lower()
        phone = contact[1]
        if not (phone.isdigit() and (13 >= len(phone) >=9)):
            return print("Invalid phone number.Try again.")
        CONNTACTS[name] = phone
        print("Phone add sucesfully")

    @error_func
    def phone_func():
        contact = input("Enter name: ")
        contact = contact.strip().lower()
        print (CONNTACTS[contact])
   

    def quit_func():
        print("Good bye!")
        return quit()


    COMANDS = {
        "exit":quit_func,
        "good bye":quit_func,
        "close":quit_func,
        "hello":greet_func,
        "show all":show_func,
        "change" : change_func,
        "add" : add_func,
        "phone":phone_func
    }

    while True:
        command = input("Enter command: ")
        command = command.strip()
        
        if command not in COMANDS:
            print ("Unknown command!")
            continue

        COMANDS[command]()

        


if __name__ == "__main__":
    exit(main())