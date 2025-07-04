import Car
class CustomError(Exception):
    def __init__(self, value, message="src.practiceCode.Car.Car:__init__:Invalid input provided"):
        self.value = value
        self.message = message
        super().__init__(f"{message}: {value}")

try:
    # a = Car.Car(2025)
    a = 10/0
# except TypeError:
#     raise TypeError
except Exception as e:
    raise CustomError(e)




