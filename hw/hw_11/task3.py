def longest_word(string):
    string = string.split()
    return max(string, key=len)


string = 'My realy long sting whichILoove'
print(longest_word(string))
