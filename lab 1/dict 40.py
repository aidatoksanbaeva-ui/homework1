import string
def analyze_dict_keys(d):
    result = set()
    for k in d.keys():
        if isinstance(k, str) and not any(c.isdigit() for c in k):
            for c in k:
                if c.isalpha():
                    result.add(c)
    return result
d = {
    "apple": 1,
    "b4nana": 2,
    "cat!": 3,
    "door": 4,
    123: 5,
    "ele phant": 6
}
print(analyze_dict_keys(d))