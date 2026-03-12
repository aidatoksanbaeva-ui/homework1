def count_leaf_values(d):
    count = 0
    for v in d.values():
        if isinstance(v, dict):
            count += count_leaf_values(v)
        elif isinstance(v, list):
            count += len(v)
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