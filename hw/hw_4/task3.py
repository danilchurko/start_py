def count(first_num, second_num):

    if first_num < second_num:
        print(first_num)
        count(first_num + 1, second_num)

    elif first_num > second_num:
        print(first_num)
        count(first_num - 1, second_num)

    else:
        print(first_num)


first_num = int(input())
second_num = int(input())
count(first_num, second_num)
