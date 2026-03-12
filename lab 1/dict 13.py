def invert_dict_strict(d):
    result={}
    value_counts={}
    for v in d.values():
        value_counts[v]=value_counts.get(v, 0)+1
    for k, v in d.items():
        if value_counts[v]==1:
            result[v]=k
    return result
d = {
    "a": 1,
    "b": 2,
    "c": 1,
    "d": 3
}
print(invert_dict_strict(d))