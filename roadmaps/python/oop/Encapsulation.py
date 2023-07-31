# Python program to
# demostrate private members

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "Public property"
        self.__c = "Private property"
    
# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class:")
        print(self.__c)

# Driver code
obj1 = Base()
print(obj1.a) # Public Property

# Uncommenting print(obj1.c) will
# raise an AttributeError
# print(obj1.__c) # AttributeError: 'Base' object has no attribute '__c'

# Uncommenting obj2 = Derived() will
# also raise an AttributeError as
# private member of Base class
# is called inside Derived class
# obj2 = Derived() # AttributeError: 'Derived' object has no attribute '_Derived__c'