# define a class area which can calculate area of 
# side1 - circle, equivilateral traingle, square, 
# side1, side2 - rectange, isocelec, rightAngle
# side1, side2, side3 - scalar

from src.practiceCode.pythonDecorator1 import CustomDecorator

import math

class Area:

    # initialize class
    @CustomDecorator
    def __init__(self, shape, side1, side2 = 0, side3 = 0):
        self.shape = shape
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    # calculate area
    def calculateArea(self):
        match self.shape:
            case 'Circle':
                return math.pi * self.side1**2
            case 'Square':
                return self.side1**2
            case 'Rectangle':
                return self.side1 * self.side2
            case 'EquilateralTraingle':
                return math.sqrt(3)/4 * self.side1**2
            case 'RightAngleTraingle':
                return 0.5 * self.side1 * self.side2
            case _:
                pass