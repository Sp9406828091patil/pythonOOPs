class Area:

    def __init__(self, shape):
        self.shape = shape

    def calculateArea(self):
        return 23
    
a = Area('Circle')
output = a.calculateArea()

if output == 23:
    print("Test passed")
else:
    print("Test Fails")