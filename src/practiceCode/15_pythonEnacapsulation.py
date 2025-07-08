class Dog:
    def __init__(self, name, breed, age):
        self.name = name  # Public attribute
        self._breed = breed  # Protected attribute
        self.__age = age  # Private attribute
    
    def __privateFunction(self):
        print("I am private function")

    # Public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    # Getter and Setter for private attribute
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
            print(self.__age)
        else:
            print("Invalid age!")

# class fish(Dog):

#     def abc(self):
#         print(self._breed)
#         self._breed = 'BullDog'
#         print(self._breed)

#     def ghi(self):
#         print(self.__age)
        


labrador = Dog('ramu', 'labrador', 2)
labrador.__privateFunction()
# print(labrador.get_info())
# labrador.set_age(5)
# goldfish = fish('ramu', 'labrador', 2)
# goldfish.abc()
# goldfish.ghi()
# labrador.name = 'Bella'
# print(labrador.name)
# labrador.name = 'Pomerian'
# print(labrador._breed)
# print(labrador.__age)

# sealed, hidden, constant, accessibleToParticularClass