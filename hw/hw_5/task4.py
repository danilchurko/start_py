from random import randint

my_list = [randint(10, 100) for i in range(25)]
print(my_list)

i = 0
for i in range(len(my_list)):
    if my_list[i] % 2 == 0:
        i += 1
        continue
    else:
        my_list[i] = 0

print(my_list)
