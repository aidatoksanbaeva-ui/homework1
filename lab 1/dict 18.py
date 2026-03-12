def sort_dict_by_value_sum(d):
    items = []
    for k, v in d.items():
        items.append((k, sum(v)))
    items.sort(key=lambda x: (-x[1], x[0]))
    return items
d = {
    "a": [1,2,3],
    "b": [4,5],
    "c": [2,2,2]
}
print(sort_dict_by_value_sum(d))