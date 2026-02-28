def filter_sets(sets_list):
    result = []
    for s in sets_list:
        if len(s) <= 3:
            continue
        has_negative = False
        has_even = False
        for num in s:
            if num < 0:
                has_negative = True
            if num % 2 == 0:
                has_even = True
        if not has_negative and has_even:
            result.append(s)
    return result
sets_list = [
    {1, 2, 3, 4},
    {2, 4, 6, 8},
    {-1, 2, 3, 4},
    {1, 3, 5, 7}
]
print(filter_sets(sets_list))