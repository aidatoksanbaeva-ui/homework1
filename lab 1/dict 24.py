def union_of_filtered_sets(sets_list):
    result = set()
    for s in sets_list:
        for x in s:
            if x > 10 and x % 2 != 0:
                result.add(x)
    return result
sets_list = [{5, 12, 13}, {11, 14, 15}, {8, 17, 20}]
print(union_of_filtered_sets(sets_list))