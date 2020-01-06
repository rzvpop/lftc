class HashTable:
    def __init__(self, hash_fct_val=lambda x: x):
        self.__table = []
        self.__size = 0
        self.__hash_fct_val = hash_fct_val

    @staticmethod
    def __hash(value):
        key = 0
        for c in value:
            key = (key + ord(c)) % 30
        return key

    def put(self, value):
        key = self.__hash(self.__hash_fct_val(value))
        pos = [i for i, v in enumerate(self.__table) if v[0] == key]

        if len(pos) == 0:
            self.__table.append((key, [value]))
        else:
            self.__table[pos[0]][1].append(value)
        self.__size += 1

    def getSize(self):
        return self.__size

    def get(self, element):
        key = self.__hash(self.__hash_fct_val(element))
        pos = [i for i, v in enumerate(self.__table) if v[0] == key]

        if len(pos) != 0:
            for i in self.__table[pos[0]][1]:
                if self.__hash_fct_val(i) == self.__hash_fct_val(element):
                    return i
            return None
        else:
            return None

    def getTable(self):
        return self.__table

    def __str__(self):
        return str(self.__table)
