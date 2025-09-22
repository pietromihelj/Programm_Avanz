class Food:

    def __init__(self, name, category, calories):
        self.name = name
        self.category = category
        self.calories = calories


class Animale:

    common_name = "Gatto"
    calories_needed = 300

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.happiness = 0
        self.calories = 0

    def eat(self, food):
        self.calories += food.calories
        if (self.calories > self.calories_needed):
            print("Ho mangiato troppo")
            self.happiness -= 1

    def interact_with(self, animal):
        self.happiness += 1
        print(f"Sto giocando con {animal.name}")

    def __str__(self):
        return f"Sono un {self.common_name} di nome {self.name}"


class Carnivoro(Animale):

    def eat(self, food):
        if isinstance(food,Animale):
            print("non mangiare i tuoi amici")
        if food.category == "carne":
            super().eat(food)
        else:
            print(f"Sono un carnivoro, non posso mangiare {food.name}")
        


class Erbivoro(Animale):

    def eat(self, food):
        if food.category == "vegetale":
            super().eat(food)
        else:
            print(f"Sono un erbivoro, non posso mangiare {food.name}")


class AnimaleDomestico(Animale):

    def pet(self):
        self.happiness += 1
        print("Mi stanno coccolando")


class Gatto(Carnivoro, AnimaleDomestico):

    common_name = "Gatto"
    calories_needed = 300

    def follow_laser_pointer(self):
        self.happiness += 1
        print("Inseguo il puntatore laser!")


class Coniglio(Erbivoro, AnimaleDomestico):

    common_name = "Coniglio"
    calories_needed = 200
    category = "carne"
    
class Panda(Erbivoro):

    common_name = "Panda"
    calories_needed = 1100

    def interact_with(self, animal):
        self.happiness -= 1
        print(f"Sono un panda solitario, non voglio giocare con {animal.name}")

class Passerotto(Carnivoro, AnimaleDomestico):
    common_name="Passerotto"
    calories_needed = 50
    category = "carne"
    def svolazzo(self):
        self.happiness +=1
        print("svolazzo libero e felice")

class Bambino(Erbivoro, AnimaleDomestico):
    common_name="Bambino"
    calories_needed = 200
    def parlo(self):
        print("ciao")

carota = Food("carota", "vegetale", 40)
bistecca = Food("bistecca", "carne", 270)

attila = Gatto("Attila", 7)
roger = Coniglio("Roger", 2)
john = Panda("John", 3)
pit = Passerotto('Pit',0.5)
frank = Bambino("Frank", 2)

attila.eat(roger)
attila.eat(bistecca)
roger.eat(carota)
roger.eat(bistecca)

attila.follow_laser_pointer()

attila.interact_with(roger)
roger.interact_with(attila)
john.interact_with(roger)

print(attila)
print(roger)
print(john)

attila.pet()
roger.pet()
pit.svolazzo()
frank.parlo()