from Utils.HashTable import HashTable


class SymbolTable:
    def __init__(self):
        self.__table = HashTable(lambda x: x[0])

    def putSymbol(self, value):
        self.__table.put((value, self.__table.getSize()))

    def getCode(self, value):
        element = self.__table.get((value, 0))
        if element is not None:
            return element[1]
        return None

    def getTable(self):
        return self.__table

    def __str__(self):
        lst = []
        for i in self.__table.getTable():
            lst += i[1]

        return str(lst)
