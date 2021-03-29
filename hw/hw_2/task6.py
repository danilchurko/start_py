tpl = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
X = abs(float(input("Please enter number --> ")))

if X in tpl:
    print("Your number", X, "contained in tuple")
else:
    print("Your number", X, "don't contained in tuple")
