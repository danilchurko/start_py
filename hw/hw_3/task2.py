number = abs(float(input("Type some number:")))

first_digit = (int(number * 10) % 10)
second_digit = (int(number * 100) % 10)
whole_part = int(number - ((first_digit * 10 + second_digit) / 100))

print("Whole part - ", whole_part)
print("Fraction - ", round(number - whole_part, 2))
