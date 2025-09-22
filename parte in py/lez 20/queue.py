class Queue:

    def __init__(self):
        self.__data = []
        self.__size = 0

    def add(self, x):
        self.__data.append(x)
        self.__size = self.__size + 1

    def remove(self):
        x = self.__data[0]
        self.__data = self.__data[1:]
        self.__size = self.__size - 1
        return x

    def empty(self):
        return self.__data == []

    def Qsize(self):
        return self.__size
    
    @classmethod
    def fromlist(cls, lst):
        q = cls()
        for elem in lst:
            q.add(elem)
        return q

q1 = Queue()
q2 = Queue()

q1.add(3)
q1.add(4)

q2.add(1)

print(q2.Qsize())
print(q2.remove())

q3

while (not q1.empty()):
    print(q1.remove())
