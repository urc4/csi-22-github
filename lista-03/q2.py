class Engineer:
    def __init__(self):
        print("I am an engineer and I make 100k per year")

    def talk(self):
        print("pi equals three")


class Entrepeneur:
    def __init__(self):
        print("I am an entrepeneur and I lose 100k per year.")

    def talk(self):
        print("stocks are going down")


class Graduate(Engineer, Entrepeneur):
    def __init__(self):
        super().__init__()
        print("I am a graduate from UCLA and I make nothing per year.")

    def talk(self):
        super().talk()


class UnderGraduate(Graduate):
    def __init__(self):
        super().__init__()
        print("I am an undergraduate from UCLA and I make nothing per year.")

    def talk(self):
        super().talk()


gus = Graduate()
gus.talk()
print(gus.__class__.__mro__)

tavo = UnderGraduate()
tavo.talk()
print(tavo.__class__.__mro__)
