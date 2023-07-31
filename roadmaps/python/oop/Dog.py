class Dog:
    # class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name

    # Methods
    def speak(self):
        print("My name is {}".format(self.name))
    
# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1)) # Rodger is a mammal
print("Tommy is also a {}".format(Tommy.__class__.attr1)) # Tommy is also a mammal

# Accessing instance attributes
print("My name is {}".format(Rodger.name)) # My name is Rodger
print("My name is {}".format(Tommy.name)) # My name is Tommy

# Accessing class methods
Rodger.speak() # My name is Rodger
Tommy.speak() # My name is Tommy