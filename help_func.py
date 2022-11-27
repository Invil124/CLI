from classes import AddressBook
import os
import pickle
from output_logic import TypeStr


def error_func(handler):
    def wrapper(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        except IndexError as error_int:
            return "Give me name and phone please", TypeStr.ERROR
        except KeyError as er:
            return "Wrong name try aggain", TypeStr.ERROR
        except TypeError:
            return "Wrong commands type", TypeStr.ERROR
        except ValueError as e:
            return e.args[0], TypeStr.ERROR
        except Exception as e:
            return e.args, TypeStr.ERROR
    return wrapper


def load_contacts(): # завантажує книгу контактів 
    if os.path.exists("dump.pickle"):
        with open("dump.pickle","rb") as fh:
            return pickle.load(fh)
    else:
        return AddressBook()


def save_contacts(data): #  зберігає книгу контактів 
    with open("dump.pickle","wb") as fh:
        pickle.dump(data,fh)


def make_string_phones(record):
    phones = ", ".join(list(map(lambda x : x.value, record.phones)))
    return phones