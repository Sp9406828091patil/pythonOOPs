# Inverted triangle

# Diamond pattern

# Hollow triangle

rows = 6
symbol = "@"
j = 1
for i in range(rows + 2):
    if i < rows:
        if i == 3:
            spaces = rows - 2*i +1
            stars = 4 * i - 3
            print(" " * spaces + symbol * stars)

            pass
        else:
            spaces = rows - i
            stars = 2 * i - 1
            print(" " * spaces + symbol * stars)
    else:
        spaces = i - 2
        stars = (i-3*j)
        print(" " * spaces + symbol * stars)
        j += 1



