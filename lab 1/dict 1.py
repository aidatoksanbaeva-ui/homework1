def invert_unique(d):
    new_dict = {}
    for key in d:
        value = d[key]
        if value not in new_dict:
            new_dict[value] = []
        if key not in new_dict[value]:
            new_dict[value].append(key)
    return new_dict
d = {'a': 1, 'b': 2, 'c': 1, 'd': 2}
print(invert_unique(d))