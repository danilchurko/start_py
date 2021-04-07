dict_raw = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None}

dict_edit = {k: v for k, v in dict_raw.items() if v is not None}

print(dict_edit)
