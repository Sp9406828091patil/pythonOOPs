class InvalidInputError(Exception):

    def __init__(self, funcName, args):
        self.functionName = funcName
        self.errorType = type(args).__name__
        self.message = str(args)
        self.getValueAndMessage()
        self.displayErrorMessage()

    def getValueAndMessage(self):
        parts = self.message.split(":")
        self.message = parts[0]
        interValue = parts[1].strip().split("'")
        self.value = interValue[1]
        
    def displayErrorMessage(self):
        if isinstance(complex(self.value), complex):
            errorMessage = f"{self.errorType}:{self.message}. The enter input {self.value} is complex"
        elif isinstance(self.value, str):
            errorMessage = f"{self.errorType}:{self.message}. The enter input {self.value} is string"
        else:
            errorMessage = f"{self.errorType}:{self.message}. The enter input {self.value} is not of numerical type"
        print(f"{self.functionName}:{errorMessage}")

try:
    newNum = int(input("Enter your number : ")) # str, complex, alphanumeric
    print(newNum)
except Exception as e:
    InvalidInputError("PythonDecorator:ClassName:FunctionName", e)
    



