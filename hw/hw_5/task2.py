result = []
while True:
    word = input('Type words: ')

    if word == 'stop':
        break
    else:
        result.append(word)

print(f'LEN list() - {len(result)} words')
print(f'Sum of LEN words in list() - {sum(list(len(i) for i in result))} simbols')
