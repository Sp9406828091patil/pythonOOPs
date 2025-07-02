class MyNumbers:
  
  def __init__(self, myStr):
    self.myStr = myStr
    self.index = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.index == len(self.myStr):
      raise StopIteration
    else:
      newName = self.myStr[self.index]
      self.index += 1
      return newName
    
myNumber = MyNumbers("aboli")
myIter = iter(myNumber)
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))