number = abs(float(input("Type some number:")))

fraction = round(number % 1, 2)

print("Whole part - ",  number - fraction)
print("Fraction - ", fraction)
