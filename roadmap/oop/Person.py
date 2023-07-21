"""
Python code to demostrate how parent constructors
are called.
"""

# Parent Class
class Person(object):
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("ID number is {}".format(self.idnumber))

# Child Class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # Invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("ID number is {}".format(self.idnumber))
        print("Post: {}".format(self.post))


# creation of an object variable or an instance
a = Employee("Cesar", 886012, 200000, "Manager")

# Calling a funtion of the class Person using
# its instance
a.display()
a.details()

'''
Cesar
886012
My name is Cesar
ID number is 886012
Post: Manager
'''