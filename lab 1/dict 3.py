def merge_dicts_sum(d1, d2):
    new_dict = {}
    for key in d1:
        new_dict[key] = d1[key]
    for key in d2:
        if key in new_dict:
            new_dict[key] += d2[key]
        else:
            new_dict[key] = d2[key]
    return new_dict
d1 = {'a': 2, 'b': 3}
d2 = {'b': 4, 'c': 5}
print(merge_dicts_sum(d1, d2))