import re

istring = input(str("Input password:"))

a = 0
if re.search(r"\w[a-z]", istring):
    pass
else:
    a = 1
    print("Хотя бы одна маленькая буква")

    if re.search(r"\w[A-Z]", istring):
        pass
    else:
        a = 1
        print("Хотя бы одна большая буква")

        if re.search(r"\d", istring):
            pass
        else:
            a = 1
            print("Хотя бы одна цифра")

            if re.search(r"\W", istring):
                pass
            else:
                a = 1
                print("Хотя бы однид символ $#@-+= ")

                if len(istring) > 8:
                    pass
                else:
                    a = 1
                    print("Хотя бы 8 символов")

if a == 0:
    print("password accepted")

