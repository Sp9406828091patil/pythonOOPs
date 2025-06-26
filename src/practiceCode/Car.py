class Car:
    wheel = 4
    steering = 1
    windows = 4

    # instantiate a class
    def __init__(self, seat, brandName):
        self.seat = seat
        self.brand = brandName

    # vehicle weight
    def getVehicleWeight(self, fuelTankCapacity):
        return str(100 * self.seat + fuelTankCapacity + 
                    self.wheel + self.steering + self.windows) + " kg"

class Aboli:
    pass