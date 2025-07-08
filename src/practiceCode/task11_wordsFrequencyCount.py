# get the frequency of each char in string

myString = "MyNameIsSaanvi"
uniqueChars = set(myString)

freq = {}
for eachChar in uniqueChars:
    freq[eachChar] = myString.count(eachChar)
    
print(freq)


