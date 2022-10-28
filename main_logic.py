
from classes import Name,Phone,Record
from help_func import error_func, load_contacts, save_contacts, make_string_phones

CONNTACTS = load_contacts() # загружає список контактів, якщо його немає то створює пустий


def greet_func(*args): #вітання 
    return "How can I help you?"

def quit_func(*args): # функція зберігає данні і виходить з боту.
    save_contacts(CONNTACTS)
    return "Good bye!"

def show_func(*args):
    show_names = list()
    for name, record in CONNTACTS.data.items():
        name = name
        phone = make_string_phones(record) # це потрібно, бо атрибут phones в класі Records це список з екземплярів класу Phone 
        show_names.append(f"{name}: {phone}")
    return show_names
        
def change_func(*args):
    contact = args[0] 

    name = Name(contact[0])
    old_phone = contact[1].replace("+","")
    new_phone = Phone(contact[2].replace("+",""))
  
    record = CONNTACTS.data[name.value]
    phone_numbers = list(map(lambda x : x.value, record.phones))
    index = phone_numbers.index(old_phone) # знаходимо індекс старого телефону в списку
    record.change_phone(index,new_phone) # змінюємо телефон за допомогою індексу 

    return "Phone successfully changed"

def add_record_func(*args):
    contact = args[0] 
    record = Record(*contact)
    CONNTACTS.add_record(record) # додає до CONTACTS(екземпляр AdressBook) екземпляри класу Records
    return "Record add sucesfully"

def phone_func(*args): #показує телефони контакту
    contact = args[0]
    name = contact[0]
    record = CONNTACTS.data[name]
    phones = make_string_phones(record)
    return (f"{phones}")
   
def  add_num_func(*args): # додає ще один норер до контакту
    conntact = args[0]
    name = conntact[0]
    new_phone = Phone(conntact[1].replace("+",""))

    record = CONNTACTS.data[name]
    record.add_phone(new_phone)
    
    return "New phone add"
    
def del_num_func(*args): # видаляє телефонні номери
    conntact = args[0]
    name = conntact[0]
    old_phone = conntact[1].replace("+","")

    record = CONNTACTS.data[name]

    phone_numbers = list(map(lambda x : x.value, record.phones))
    index = phone_numbers.index(old_phone) # знаходимо індекс старого телефону в списку
    record.delite_phone(index) # змінюємо телефон за допомогою індексу 
    
    return "Phones sucesfully delete"
    
def day_to_birthday_func(*args): #рахує дні до дня народження
    conntact = args[0]
    name = conntact[0]
    record = CONNTACTS.data[name]
    return record.days_to_birthday

def add_birthday_func(*args): #довзволяє доадти існуючому контакту день народження 
    conntact = args[0]
    name = conntact[0]
    record = CONNTACTS.data[name]
    record.add_birthday(conntact[1])
    return "Birthday sucesfully add"

def iter_concntact(max_iters): # AddressBook реалізує метод iterator, який повертає генератор за записами AddressBook і за одну ітерацію повертає уявлення для N записів.
    counter = 0
    max_iters = int(max_iters[0])
    generator = CONNTACTS.itrerator()
    show_names = list()
    for record in generator:
        counter += 1
        name = record.name.value
        phones = make_string_phones(record)
        show_names.append(f"{name}: {phones}")
        if counter >= max_iters:
            break
    return show_names
    
def find_contact(*args): # функція яка знаходить контакт 
    search_inputr = args[0][0]
    generator = CONNTACTS.itrerator()
    search_result = list()
    for record in generator:
        phones = make_string_phones(record)
        string = f"{record.name.value} {phones}"
        if search_inputr in string:
            search_result.append(string)
    return search_result

@error_func
def entered_command(command):
    
    command = command.strip().split(" ")

    commands = {
        "exit":quit_func,
        "good":quit_func,
        "close":quit_func,
        "hello":greet_func,
        "show":show_func,
        "change" : change_func,
        "add" : add_record_func,
        "phone":phone_func,
        "add_number": add_num_func,
        "delete_number": del_num_func,
        "add_birthday": add_birthday_func,
        "birthday":day_to_birthday_func,
        "iter_contact":iter_concntact,
        "find":find_contact} 
    
    if command[0] not in commands:
        return "Command not found"
    return commands[command[0]](command[1:])