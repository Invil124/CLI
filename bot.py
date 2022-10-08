
from collections import UserDict

class AddressBook(UserDict):
    def add_record(self,record):
        self.data[record.name.value] = record

class Field:
    pass

class Name(Field):
    def __init__(self,name):
        self.value = name

class Phone(Field):
    def __init__(self,phone):
        self.value = phone

class Record:
    def __init__(self,name,phone = None):
        self.phones = list()
        self.phones.append(phone)
        self.name = name
    
    def add_phone(self,new_phone):
        self.phones.append(new_phone)

    def change_phone(self,new_phone):
        self.phones.clear()
        self.phones.append(new_phone)

    def delite_phone(self):
        self.phones.clear()

    
CONNTACTS = AddressBook() # Екземпляр класу AdressBook

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
    for name, record in CONNTACTS.data.items():
        name = name.title()
        phone = list(map(lambda x : x.value, record.phones)) # це потрібно, бо атрибут phones в класі Records це список з екземплярів класу Phone 
        print(f"{name}: {phone}")
        
@error_func
def change_func(*args):
    contact = args[0] 

    if len(contact) < 2:
        return print("Inpunt current name and new phone:")

    name = Name(contact[0].lower())
    new_phone = Phone(contact[1].replace("+",""))

    if name.value not in CONNTACTS.data:
        return print("Current name not find.")

    if not (new_phone.value.isdigit() and (13 >= len(new_phone.value) >=9)):
        return print("Invalid phone number.Try again.")    
    
    record = CONNTACTS.data[name.value]
    record.change_phone(new_phone)

    print("Phone successfully changed")

@error_func
def add_func(*args):
    contact = args[0] 
    name = Name(contact[0].lower())
    phone = Phone(contact[1].replace("+",""))

    if not (phone.value.isdigit() and (13 >= len(phone.value) >=9)):
        return print("Invalid phone number.Try again.")

    record = Record(name,phone)
    CONNTACTS.add_record(record)
    print("Phone add sucesfully")

@error_func
def phone_func(*args):
    contact = args[0]
    name = contact[0].lower()
    record = CONNTACTS.data[name]
    print (f"{list(map(lambda x : x.value, record.phones))}")
   
def quit_func(*args):
    print("Good bye!")
    return quit()

@error_func
def  add_num_func(*args): # додає ще один норер до контакту
    conntact = args[0]
    name = conntact[0].lower()
    new_phone = Phone(conntact[1].replace("+",""))
    record = CONNTACTS.data[name]
    record.add_phone(new_phone)
    print("New phone add")
    
@error_func
def del_num_func(*args): # видаляє телефонні номери
    conntact = args[0]
    name = conntact[0].lower()
    record = CONNTACTS.data[name]
    record.delite_phone()
    print("Phone sucesfully delete")
    

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
        "phone":phone_func,
        "add_number": add_num_func, # нова функція 
        "delete_number": del_num_func} # нова функція 
    
    if command[0] not in COMANDS:
        return print("Command not found")
    COMANDS[command[0]](command[1:])



def main():

    while True:
        command = input("Enter command: ")
        entered_command(command)
        

if __name__ == "__main__":
    exit(main())