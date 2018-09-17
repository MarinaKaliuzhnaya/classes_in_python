class Animal():
    def __init__(self, tail, paw, wool):
        self.tail = 1
        self.paw = 4
        self.wool = True


class Dog (Animal):
    def __init__(self, tail, paw, wool):
        Animal.__init__(self, tail, paw, wool)

    def say_something(self):
        print("Woof-woof")


class Cat(Animal):
    def __init__(self, tail, paw, wool):
        Animal.__init__(self, tail, paw, wool)

    def say_something(self):
        print("Meow-meow")


class SphynxCat(Cat):
    def __init__(self, tail, paw, wool):
        Animal.__init__(self, tail, paw, wool)
        self.wool = False

    def say_something(self):
        print("murr-murr")


class Rooster(Animal):
    def __init__(self, tail, paw, wool):
        Animal.__init__(self, tail, paw, wool)
        self.paw = 2
        self.wool = False

    def say_something(self):
        print("Cocorico")

some_animal = Animal(0, 0, 0)
print (some_animal.tail)
print (some_animal.paw)
print (some_animal.wool)

kitty = Cat(0,0,0)
print (kitty.tail, kitty.paw, kitty.wool,)
print (kitty.say_something())

petya = Rooster (0,0,0)
print (petya.say_something())
print (petya.tail, petya.paw, petya.wool)



