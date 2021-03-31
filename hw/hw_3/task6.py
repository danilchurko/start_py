first_x = int(input())
first_y = int(input())

second_x = int(input())
second_y = int(input())

dist_x = abs(first_x - second_x)
dist_y = abs(first_y - second_y)

if dist_x == 1 and dist_y == 2 or dist_x == 2 and dist_y == 1:
    print("CAN")
else:
    print("CAN'T")
