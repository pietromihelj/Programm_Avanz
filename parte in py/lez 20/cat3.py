class Cat:

    species = "Felis catus"

    def __init__(self, name, age):
        self.name = name
        self.age = age


tom = Cat("Tom", 13)
print(tom.name)
print(tom.species)

gerry = Cat("Gerry", 17)
print(gerry.name)
print(tom.species)

tom.species = "gatto"
Cat.species = "gattino arancione"

print(Cat.species)
print(tom.species)
print(gerry.species)
