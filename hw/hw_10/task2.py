def palindrop_check():
    c = input()
    if c != c[::-1]:
        print("It's not palindrome")
    else:
        print("It's palindrome")


palindrop_check()
