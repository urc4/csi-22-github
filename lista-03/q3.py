class Animal:
    pass


class Mammal(Animal):
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"can milk."

    def get_name(self):
        return self.name


class Reptile(Animal):
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"is cold blooded."

    def get_name(self):
        return self.name


class Bird(Animal):
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"can fly."

    def get_name(self):
        return self.name


mammal = Mammal("Marley")
reptile = Reptile("Crocs")
bird = Bird("Larry")

print(mammal.get_name())
print(mammal.info())
print(reptile.get_name())
print(reptile.info())
print(bird.get_name())
print(bird.info())
