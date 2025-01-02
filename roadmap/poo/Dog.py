class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks: \"{sound}\""


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

# Create instances of the Dog class
miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

# Test the instances
print(miles.species) # Canis familiaris
print(buddy.name) # Buddy
print(jack) # Jack is 3 years old
print(jim.speak("Woof")) # Jim says Woof

# To determine which class a given object belongs to, you can use the built-in type() function
print(type(miles)) # <class '__main__.JackRussellTerrier'>

# Determine if an object is an instance of a class
print(isinstance(miles, Dog)) # True

print(miles.speak()) # Miles barks: "Arf"
print(miles.speak("Grrr")) # Miles bark: "Grrr"

print(jim.speak("Woof")) # Jim barks: "Woof"
