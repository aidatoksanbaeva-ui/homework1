def sort_by_value_length(d):
    items=[]
    for key in d:
        items.append((key,d[key]))
    items.sort(key=lambda x: (len(x[1]), x[0]))
    return items
d={
    "a":"apple",
    "b":"kiwi",
    "c":"banana",
    "d":"orange",
}
print(sort_by_value_length(d))