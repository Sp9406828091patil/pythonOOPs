class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

    def acc(self):
        print("Accelerate")

class Boat():

    def play(self):
        print("Sail!")


class Plane(Car, Boat):

    def stop(self):
        print("Stopped!")

p = Plane('Boeing', '747', 2025)
p.stop()
p.move()
p.play()