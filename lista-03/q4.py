class Methods:
    class_variable = "class variable"

    def __init__(self):
        pass

    def instance_method(self):
        self.instance = "instance variable"

    @classmethod
    def class_method(cls):
        cls.class_variable = "change class variable"

    @staticmethod
    def static_method():
        static_variable = "static variable"


# Criar instancia
obj = Methods()

# Chamar metodo da instancia e imprimir seu valor
obj.instance_method()
print(obj.instance)

# Imprimir valor da variavel da classe e depois alterar seu valor e imprimir
print(Methods.class_variable)
Methods.class_method()
print(Methods.class_variable)

# Chamar metodo estatico
Methods.static_method()

# This will raise a NameError because static_variable is not defined in the global scope
print(static_variable)
