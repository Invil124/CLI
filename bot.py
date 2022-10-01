

CONNTACTS = {}

def error_func(handler):
    def wrapper(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        except IndexError as error_int:
            print("Give me name and phone please")
        except KeyError as er:
            print("Wrong name try aggain")
    return wrapper

def greet_func(*args):
    return print("How can I help you?")

def show_func(*args):
    for name, phone in CONNTACTS.items():
        name = name.title()
        print(f"{name}: {phone}")
        
@error_func
def change_func(*args):
    contact = args[0] #лист мінімум з двома аргументами
    if len(contact) < 2:
        return print("Inpunt current name and new phone:")
    name = contact[0]
    new_phone = contact[1] 
    new_phone = new_phone.replace("+","") 
    name = name.lower()
    if name not  in CONNTACTS:
        return print("Current name not find.")
    if not (new_phone.isdigit() and (13 >= len(new_phone) >=9)):
        return print("Invalid phone number.Try again.")    
    CONNTACTS[name] = new_phone
    print("Phone successfully changed")

@error_func
def add_func(*args):
    contact = args[0] #лист мінімум з двома аргументами
    name = contact[0].lower()
    phone = contact[1]
    phone = phone.replace("+","") 
    if not (phone.isdigit() and (13 >= len(phone) >=9)):
        return print("Invalid phone number.Try again.")
    CONNTACTS[name] = phone
    print("Phone add sucesfully")

@error_func
def phone_func(*args):
    contact = args[0]
    name = contact[0].lower()
    print (CONNTACTS[name])
   
def quit_func(*args):
    print("Good bye!")
    return quit()

@error_func
def entered_command(command):
    
    command = command.strip().split(" ")

    COMANDS = {
        "exit":quit_func,
        "good":quit_func,
        "close":quit_func,
        "hello":greet_func,
        "show":show_func,
        "change" : change_func,
        "add" : add_func,
        "phone":phone_func}
    
    if command[0] not in COMANDS:
        return print("Command not found")
    COMANDS[command[0]](command[1:])



def main():

    while True:
        command = input("Enter command: ")
        entered_command(command)
        

if __name__ == "__main__":
    exit(main())