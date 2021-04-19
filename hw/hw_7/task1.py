def spliter(func):
    def sp(sentense):
        sent = sorted(sentense.split(' '))
        func(sent)
    return sp


@spliter
def string_back(string_temp):
    return print(string_temp)


str_user = input('Type your string --> ')
string_back(str_user)

