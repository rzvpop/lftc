from Utils.HashTable import HashTable


class PIF:
    def __init__(self):
        self.__elements = []

    def add_to_end(self, value):
        if isinstance(value, tuple):
            self.__elements.append(value)
        elif isinstance(value, int):
            self.__elements.append((value, -1))

    def getElements(self):
        return self.__elements

    def __str__(self):
        return str(self.__elements)
