class Mammal:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"I can milk."

    def get_name(self):
        return self.name


class Reptile:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"I am cold blooded."

    def get_name(self):
        return self.name


class Bird:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"I can fly."

    def get_name(self):
        return self.name


mammal = Mammal("Marley")
reptile = Reptile("Crocs")
bird = Bird("Larry")

print(mammal.info())
print(mammal.get_name())
print(reptile.info())
print(reptile.get_name())
print(bird.info())
print(bird.get_name())
