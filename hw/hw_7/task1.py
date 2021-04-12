def spliter(func):
    def sp(sentense):
        print(sorted(sentense.split(' ')))
        func(sentense)
    return sp


@spliter
def string_back(string_temp):
    return string_temp


str_user = input('Type your string --> ')
print('dict:', str(string_back(str_user)))

