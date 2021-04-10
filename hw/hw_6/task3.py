values = ['a', 'b', 'c', 'd', 'e']
keys = []

for i in enumerate(values):
    keys.append(i)

new_dict = {k: v for k, v in keys}

print(new_dict)
