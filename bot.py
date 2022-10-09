
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

    def change_phone(self,index_oldphone,new_phone):
        self.phones.pop(index_oldphone)
        self.phones.append(new_phone)

    def delite_phone(self,phone_index):
        self.phones.pop(phone_index)

    
CONNTACTS = AddressBook() # Екземпляр класу AdressBook

def error_func(handler):
    def wrapper(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        except IndexError as error_int:
            return "Give me name and phone please"
        except KeyError as er:
            return "Wrong name try aggain"
        except TypeError:
            return "Wrong commands type"
        except ValueError as e:
            return e.args[0]
        except Exception as e:
            return e.args
    return wrapper

def greet_func(*args):
    return "How can I help you?"

def show_func(*args):
    show_names = list()
    for name, record in CONNTACTS.data.items():
        name = name.title()
        phone = ", ".join(list(map(lambda x : x.value, record.phones))) # це потрібно, бо атрибут phones в класі Records це список з екземплярів класу Phone 
        show_names.append(f"{name}: {phone}\n")
    return show_names
        
@error_func
def change_func(*args):
    contact = args[0] 

    name = Name(contact[0].lower())
    old_phone = contact[1].replace("+","")
    new_phone = Phone(contact[2].replace("+",""))

    if not (new_phone.value.isdigit() and (13 >= len(new_phone.value) >=9)):
        return "Invalid phone number.Try again."    
    
    record = CONNTACTS.data[name.value]
    phone_numbers = list(map(lambda x : x.value, record.phones))
    index = phone_numbers.index(old_phone) # знаходимо індекс старого телефону в списку
    record.change_phone(index,new_phone) # змінюємо телефон за допомогою індексу 

    return "Phone successfully changed"

@error_func
def add_func(*args):
    contact = args[0] 
    name = Name(contact[0].lower())
    phone = Phone(contact[1].replace("+",""))

    if not (phone.value.isdigit() and (13 >= len(phone.value) >=9)):
        return "Invalid phone number.Try again."

    record = Record(name,phone)
    CONNTACTS.add_record(record) # додає до CONTACTS(екземпляр AdressBook) екземпляри класу Records
    return "Phone add sucesfully"

@error_func
def phone_func(*args):
    contact = args[0]
    name = contact[0].lower()
    record = CONNTACTS.data[name]
    phones = ", ".join(list(map(lambda x : x.value, record.phones)))
    return (f"{phones}")
   
def quit_func(*args):
    return "Good bye!"

@error_func
def  add_num_func(*args): # додає ще один норер до контакту
    conntact = args[0]
    name = conntact[0].lower()
    new_phone = Phone(conntact[1].replace("+",""))

    record = CONNTACTS.data[name]
    record.add_phone(new_phone)
    
    return "New phone add"
    
@error_func
def del_num_func(*args): # видаляє телефонні номери
    conntact = args[0]
    name = conntact[0].lower()
    old_phone = conntact[1].replace("+","")

    record = CONNTACTS.data[name]

    phone_numbers = list(map(lambda x : x.value, record.phones))
    index = phone_numbers.index(old_phone) # знаходимо індекс старого телефону в списку
    record.delite_phone(index) # змінюємо телефон за допомогою індексу 
    
    return "Phones sucesfully delete"
    

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
        return "Command not found"
    return COMANDS[command[0]](command[1:])



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