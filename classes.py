from collections import UserDict
from datetime import datetime
import re


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def itrerator(self): # ITERATOR
        counter = 0
        show_names = list(self.data.values())

        while counter <= len(show_names)-1:
            
            yield show_names[counter]
            counter +=1 


class Field():
    def __init__(self, value):
        self.value = value


class Name(Field):
    __name = None


class Phone(Field):
    __value = None
    
    @property
    def value(self):
        return self.__value

    @value.setter 
    def value(self,phone):
        if not (phone.isdigit() and (13 >= len(phone) >=9)):
            raise Exception("Invalid phone number.Try again.") 
        
        self.__value = phone


class Birthday(Field): 
    __value = None

    @property
    def value(self):
        return self.__value

    @value.setter 
    def value(self,birthday):

        patern = r"[0,1,2,3]\d\.[1][0,1,2]|[0,1,2,3]\d\.[0]\d"
        match = re.search(patern,birthday)

        if not match:
            raise ValueError("input DATE.MONTH")

        birthday = datetime.strptime(birthday,"%d.%m")
        birthday = birthday.replace(year=datetime.now().year)
        self.__value = birthday
        
        
class Record:
    
    def __init__(self, name, phone=None, birthday=None):
        self.phones = list()
        self.name = Name(name)

        if phone:
            self.phones.append(Phone(phone))

        if birthday:
            self.birthday = Birthday(birthday)
    
    def add_phone(self,new_phone):
        self.phones.append(new_phone)
    
    def add_birthday(self,date):
        self.birthday = Birthday(date)

    def change_phone(self, index_oldphone, new_phone):
        self.phones.pop(index_oldphone)
        self.phones.append(new_phone)
    
    @property
    def days_to_birthday(self):
        current_datetime = datetime.now()
        birthday = self.birthday.value
        if current_datetime > birthday:
            birthday = birthday.replace(year=datetime.now().year + 1)
    
        difference = birthday - current_datetime
        return f"{difference.days} days left."

    def delite_phone(self,phone_index):
        self.phones.pop(phone_index)
