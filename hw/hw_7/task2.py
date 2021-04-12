def convert(numb_tmp, letter_tmp):
    numb_k, numb_c, numb_f = 0, 0, 0
    if letter_tmp == 'K':
        numb_k = numb_tmp
        numb_c = numb_tmp - 273.15
        numb_f = numb_tmp * 1.8 - 459.76
    elif letter_tmp == 'C':
        numb_k = numb_tmp + 273.15
        numb_c = numb_tmp
        numb_f = numb_tmp * 1.8 + 32
    elif letter_tmp == 'F':
        numb_k = (numb_tmp + 459.67) / 1.8
        numb_c = (numb_tmp - 32) / 1.8
        numb_f = numb_tmp
    else:
        print('Try again')
    return print('K = {:.2f} | C = {:.2f} | F = {:.2f}'.format(numb_k, numb_c, numb_f))


numb = float(input("Enter a temperature value: "))
letter = str(input("K, C, F ---> ").upper())

convert(numb, letter)
