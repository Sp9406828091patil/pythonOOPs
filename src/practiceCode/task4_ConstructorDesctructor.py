#Create a Person class with a constructor that sets name and age, 
#and a destructor that prints a message when the object is deleted.

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("obj is deleted")

p = Person('Sagar', '35')
del p
print(p)




