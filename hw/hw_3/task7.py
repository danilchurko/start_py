some_numb = int(input("Type some number and I count it as a factorial:"))

factorial = 1

for i in range(2, some_numb + 1):
    factorial *= i

print(some_numb, "! =", factorial)
