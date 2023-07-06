
from classes import Name,Phone,Record
from help_func import error_func, load_contacts, save_contacts, make_string_phones
from output_logic import TypeStr

CONNTACTS = load_contacts() # загружає список контактів, якщо його немає то створює пустий


def greet_func(*args): 
    return "How can I help you?", TypeStr.REQUEST


def quit_func(*args): 
    save_contacts(CONNTACTS)
    return "Good bye!", TypeStr.REQUEST


def show_func(*args):
    show_names = dict()
    for name, record in CONNTACTS.data.items():
        name = name
        phone = make_string_phones(record) # це потрібно, бо атрибут phones в класі Records це список з екземплярів класу Phone 
        show_names[name] = phone
    return show_names, TypeStr.REQUEST


def change_func(*args):
    contact = args[0] 

    name = Name(contact[0])
    old_phone = contact[1].replace("+","")
    new_phone = Phone(contact[2].replace("+",""))
  
    record = CONNTACTS.data[name.value]
    phone_numbers = list(map(lambda x : x.value, record.phones))
    index = phone_numbers.index(old_phone) # знаходимо індекс старого телефону в списку
    record.change_phone(index,new_phone) # змінюємо телефон за допомогою індексу 

    return "Phone successfully changed", TypeStr.LOG


def add_record_func(*args):
    contact = args[0] 
    record = Record(*contact)
    CONNTACTS.add_record(record) # додає до CONTACTS(екземпляр AdressBook) екземпляри класу Records
    return "Record add sucesfully", TypeStr.LOG


def phone_func(*args): 
    contact = args[0]
    name = contact[0]
    record = CONNTACTS.data[name]
    phones = make_string_phones(record)
    return (f"{phones}"), TypeStr.REQUEST


def  add_num_func(*args): 
    conntact = args[0]
    name = conntact[0]
    new_phone = Phone(conntact[1].replace("+",""))

    record = CONNTACTS.data[name]
    record.add_phone(new_phone)
    
    return "New phone add", TypeStr.LOG


def del_num_func(*args):
    conntact = args[0]
    name = conntact[0]
    old_phone = conntact[1].replace("+","")

    record = CONNTACTS.data[name]

    phone_numbers = list(map(lambda x : x.value, record.phones))
    index = phone_numbers.index(old_phone) # знаходимо індекс старого телефону в списку
    record.delite_phone(index) # змінюємо телефон за допомогою індексу 
    
    return "Phones sucesfully delete", TypeStr.LOG


def day_to_birthday_func(*args): 
    conntact = args[0]
    name = conntact[0]
    record = CONNTACTS.data[name]
    return record.days_to_birthday, TypeStr.REQUEST


def add_birthday_func(*args):
    conntact = args[0]
    name = conntact[0]
    record = CONNTACTS.data[name]
    record.add_birthday(conntact[1])
    return "Birthday successfully add", TypeStr.LOG


def iter_concntact(max_iters): 
    counter = 0
    max_iters = int(max_iters[0])
    generator = CONNTACTS.itrerator()
    show_names = dict()
    for record in generator:
        counter += 1
        name = record.name.value
        phones = make_string_phones(record)
        show_names[name] = phones
        if counter >= max_iters:
            break
    return show_names, TypeStr.REQUEST


def find_contact(*args):  
    search_inputr = args[0][0]
    generator = CONNTACTS.itrerator()
    search_result = dict()
    for record in generator:
        phones = make_string_phones(record)
        string = f"{record.name.value} {phones}"
        if search_inputr in string:
            search_result[record.name.value] = phones
    return search_result, TypeStr.REQUEST


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
        return "Command not found", TypeStr.ERROR
    return commands[command[0]](command[1:])
