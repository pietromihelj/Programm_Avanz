from typing import Any


class EvenNaturals:

    def __init__(self):
        pass

    def __getitem__(self,key):
        return 2*key
    
x = EvenNaturals()

print(x[10000])

class DeafaultVector:

    def __init__(self):
        self.__data = {}

    def __getitem__(self,key):
        try:
            return self.__data[key]
        except:
            return 0
        
    def __setitem__(self,key,value):
        self.__data[key] = value
        
y = DeafaultVector()
y[10] = 100
print(y[100])
print(y[10])