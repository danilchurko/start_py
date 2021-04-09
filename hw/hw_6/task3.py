values = ['a', 'b', 'c', 'd', 'e']
keys = []

for i in range(len(values)):
    keys.append(i)

new_dict = {k: v for k, v in zip(keys, values)}

print(new_dict)
