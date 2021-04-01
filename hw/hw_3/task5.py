import random

for i in range(3):
    human_number = input("Type some number:")
    comp_num = random.randint(0, 11)

    if human_number == comp_num:
        print("You WON!!!!")
        break
    elif i == 2:
        print("You lose((((")
    else:
        print("Nah, not right. I thought number:", comp_num, "\nTry again human\n")
