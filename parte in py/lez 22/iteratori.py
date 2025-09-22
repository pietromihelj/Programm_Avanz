class MySet():
    def __init__(self):
        self._data = []
    
    def add(self,x):
        if x not in self._data:
            self._data.append(x)
    
    def __iter__(self):
        self.__pos = 0
        return self
    def __next__(self):
        if self.__pos < len(self._data):
            temp = self._data[self.__pos]
            self.__pos += 1
            return temp
        else:
            raise StopIteration
        
s = MySet()
s.add(1)
s.add(4)
s.add(7)
s.add(3)
s.add(-12)
s.add(9)
s.add(5)

for i in s:
    print(i)
