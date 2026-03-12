def update_counts(d, items):
    for item in items:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    return d
d = {"apple": 2, "banana": 1}
items = ["apple", "banana", "cherry", "apple"]
print(update_counts(d, items))