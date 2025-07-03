# from src.practiceCode.Area import Area
import math
class Perimeter():

    def __init__(self, shape, side1, side2=None):
        self.shape = shape
        self.side1 = side1
        self.side2 = side2
        # Area.__init__(self, shape, side1, side2)

    def calculatePerimeter(self):
        match self.shape:
            case 'Circle':
                return 2 * math.pi * self.side1
            case 'Square':
                return self.side1 * 4
            case 'Rectangle':
                return 2 * (self.side1 + self.side2)
            # case 'EquilateralTraingle':
            #     return math.sqrt(3)/4 * self.side1**2
            # case 'RightAngleTraingle':
            #     return 0.5 * self.side1 * self.side2
            case _:
                pass

if __name__ == "__main__":
    obj = Perimeter()
