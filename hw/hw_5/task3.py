import math


def area(par, a, b, c=0):
    half_p = a + b + c / 2
    t_area = math.sqrt(half_p * (half_p - a) * (half_p - b) * (half_p - c))
    s_area = a * b

    if par == 1:
        print('Squere area = {:.2f}'.format(s_area))
    elif par == 2:
        print('Triangl area = {:.2f}'.format(t_area))
    else:
        print('ERROR')


figure_type = int(input('Type figure type (1 - sqrt, 2 - tringl) - '))
firs_par = int(input('Type first side: '))
second_par = int(input('Type second side: '))

if figure_type == 2:
    third_par = int(input('Type third side: '))
    area(figure_type, firs_par, second_par, third_par)

else:
    area(figure_type, firs_par, second_par)
