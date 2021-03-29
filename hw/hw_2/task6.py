tpl = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
first_num = abs(float(input("Please enter number --> ")))

if first_num in tpl:
    print("Your number", first_num, "contained in tuple")
else:
    print("Your number", first_num, "don't contained in tuple")
