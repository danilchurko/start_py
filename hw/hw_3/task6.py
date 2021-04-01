first_x = int(input("Type x1 - "))
first_y = int(input("Type y1 - "))

second_x = int(input("Type x2 - "))
second_y = int(input("Type y2 - "))

dist_x = abs(first_x - second_x)
dist_y = abs(first_y - second_y)

if dist_x == 1 and dist_y == 2 or dist_x == 2 and dist_y == 1:
    print("CAN")
else:
    print("CAN'T")
