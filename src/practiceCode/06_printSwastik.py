symbol = "*"
height = 8
width = 8

for i in range(height):
    frontSpace = " " * int(width)
    backSpace = frontSpace

    if i < 4:
        if i == 0:
            print(symbol + " " * 9 + symbol + (" " + symbol) * 4)
        elif i == 3:
            # pass
            print((symbol + " ") * 4 + symbol + (" " + symbol) * 5)
        else:
            print(symbol + frontSpace + symbol)
    else:
        if i == 7:
            print((symbol + " ") * 4 + symbol + " "* 9 + symbol )
        else:
            print(" " + frontSpace + symbol + backSpace + symbol)

    
    # if i > 3:
    #     if i == 7:
    #         print((symbol + " ") * 4 + symbol + " "* 9 + symbol )
    #     else:
    #         print(" " + frontSpace + symbol + backSpace + symbol)
    # else:
        