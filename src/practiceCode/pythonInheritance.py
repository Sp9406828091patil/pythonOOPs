class Person:

    # initialize class
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        print(self.name, self.surname)

    def method1(self):
        pass

class Student(Person):

    def __init__(self, name, surname, age):
        self.age = age
        Person.__init__(self, name, surname)
        print(self.name, self.surname, self.age)

    def method2(self):
        pass


p = Student('Sagar', 'Patil', 25)
