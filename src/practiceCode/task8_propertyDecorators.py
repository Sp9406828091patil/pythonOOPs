class Employee:
    def __init__(self, name):
        self.name = name
 
    @property
    def salary(self):
        return self._salary
   
    @salary.setter
    def settingSalary(self, value):
        if value > 0:
            self._salary = value
        else:
            print('Salary is not valid')
       
a = Employee('john')
print(a.name)
 
a.settingSalary = 50000
print(a.salary)
 