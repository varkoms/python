### Classes ###

class Person:
    def __init__(self, name, surname, alias="Sin Alias"):
        self.__name = name  # Propiedad privada
        self.__surname = surname  # Propiedad privada
        self.full_name = f"{name} {surname} ({alias})"
        self.alias = alias

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.alias} esta caminando...")

my_person = Person("Cesar", "Mendoza", "Varko")

print(my_person.full_name)  # Cesar Mendoza
my_person.full_name = "Hector de Leon (El loco de los perros)"
print(my_person.full_name)  # Hector de Leon (El loco de los perros)s
# print(my_person.alias) # Varko
my_person.walk()  # Varko esta caminando
print(my_person.get_name()) # Cesar
