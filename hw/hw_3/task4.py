list_of_six = [100, 106, 112, 118, 124, 130, 136, 142, 148, 154, 160, 166, 172, 178, 184, 190, 196]

for i in range(len(list_of_six)):
    if list_of_six[i] % 5 == 0 and list_of_six[i] <= 150:
        print(list_of_six[i])
