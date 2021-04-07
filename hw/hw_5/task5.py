import math


def squere(x):
    res = [0, 0, 0]

    res[0] = x * 2
    res[1] = x * x
    res[2] = round(math.sqrt(2) * x, 2)

    return res


x_side = int(input('Side = '))

print(squere(x_side))
