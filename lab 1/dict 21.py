def count_leaf_values(d):
    count = 0
    for v in d.values():
        if type(v) == dict:
            count += count_leaf_values(v)
        elif type(v) == list:
            for item in v:
                if type(item) == dict:
                    count += count_leaf_values(item)
                else:
                    count += 1
        else:
            count += 1
    return count
d = {
    "a": 1,
    "b": [1,2,3],
    "c": {
        "c1": 4,
        "c2": [5,6]
    }
}
print(count_leaf_values(d))