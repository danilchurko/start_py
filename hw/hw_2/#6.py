tpl = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
X = int(input("Please enter number --> "))

# почему не работает?
# if X == tpl[0:9]:
# if X == tpl[0-9]:

if X == tpl[0] or X == tpl[1] or X == tpl[2] or X == tpl[3] or X == tpl[4] or X == tpl[5] or X == tpl[6] or X == tpl[7] or X == tpl[8] or X == tpl[9]:
    print("Your number", X, "contained in tuple")
else:
    print("Your number", X, "don't contained in tuple")
