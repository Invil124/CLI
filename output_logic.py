from enum import Enum
from abc import ABC, abstractmethod


class TypeStr(str, Enum):
    LOG = "log info"
    ERROR = "error text"
    REQUEST = "request info"


class OutputOperation(ABC):

    @abstractmethod
    def output_for_user(self):
        pass

    def info(self):
        pass


class LogOutputOperation(OutputOperation):
    def __init__(self, text: str, type_str: TypeStr):
        self.text = text
        self.type_str = type_str

    def output_for_user(self):
        return self.text

    def info(self):
        return self.type_str


class ErrorOutputOperation(OutputOperation):
    def __init__(self, text: str, type_str: TypeStr):
        self.text = text
        self.type_str = type_str

    def output_for_user(self):
        return self.text

    def info(self):
        return self.type_str


class RequestOutputOperation(OutputOperation):
    def __init__(self, text: dict, type_str: TypeStr):
        self.text = text
        self.type_str = type_str

    def output_for_user(self):
        if isinstance(self.text, dict):
            new_list = []
            counter = 0
            for name, phones in self.text.items():
                counter += 1
                new_list.append(f"{counter:>4}|{name:<10}|{phones:^5}|")
            return "\n".join(new_list)
        else:
            return self.text

    def info(self):
        return self.type_str


def work_with_output(operation: OutputOperation):
    output_text = operation.output_for_user()
    output_info = operation.info()
    return output_text, output_info


def output_logic(text, type_str):

    if type_str == TypeStr.ERROR:
        output = work_with_output(ErrorOutputOperation(text,type_str))
        return output[0]
    elif type_str == TypeStr.REQUEST:
        output = work_with_output(RequestOutputOperation(text, type_str))
        return output[0]
    elif type_str == TypeStr.LOG:
        output = work_with_output(LogOutputOperation(text, type_str))
        return output[0]
