class Car:

    Engine = '2.0L'

    def __init__(self, brand, model, year):
        self.brand = brand          # -> Public Variable
        self._model = model         # -> Protected Varible
        self.__year = year          # -> Private Variable

    def move(self):
        print(f"This is public variable {self.brand}")
        print(f"This is protected variable {self._model}")
        print(f"This is private variable {self.__year}")
        print(f"This is global variable {self.Engine}")

    @staticmethod
    def engineType():
        print(Car.Engine)



p = Car('Boeing', '747', 2025)
p.brand = "Mahindra"
p._model = "XUV500"
p.__year = 2030
p.Engine = "3L"

p.move()
# p.acc()
# p.engineType()
Car.engineType()