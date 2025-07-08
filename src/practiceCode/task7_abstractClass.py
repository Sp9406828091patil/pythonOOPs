# Write an abstract base class Shape with an abstract method area(). 
# Implement it in Rectangle and Circle subclasses.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        print("This is parent class")

class Rectange(Shape):
    pass

    # def area(self):
    #     print("This is rectange class")

r = Rectange()
# r.area()

s = Shape()

