def write_file():
    fname = input('Файл: ')
    f = open(fname, 'w+')
    while True:
        s = input()
        if s == '':
            break
        f.write(s+'\n')
    f.close()


write_file()
