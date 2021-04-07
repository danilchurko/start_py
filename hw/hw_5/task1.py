def is_prime(x_arg):
    if 0 < x_arg < 1000:
        if x_arg % x_arg == 0 and x_arg % 1 == 0:
            return True
        else:
            return False
    else:
        return False


x = int(input('Type number: '))
print(is_prime(x))
