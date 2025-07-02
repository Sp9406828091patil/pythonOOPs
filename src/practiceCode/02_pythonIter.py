myStr = "Aboli"
myItrStr = iter(myStr)
print(next(myItrStr))
print(next(myItrStr))
print(next(myItrStr))


for eachChar in myStr:
    print(eachChar)

for iChar in range(len(myStr)):
    print(myStr[iChar])