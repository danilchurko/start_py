def count(first_arg, second_arg):

    if first_arg < second_arg:
        print(first_arg)
        count(first_arg + 1, second_arg)

    elif first_arg > second_arg:
        print(first_arg)
        count(first_arg - 1, second_arg)

    else:
        print(first_arg)


first_arg = int(input())
second_arg = int(input())
count(first_arg, second_arg)
