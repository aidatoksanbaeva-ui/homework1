def multi_symmetric_difference(sets_list):
    if not sets_list:
        return set()
    result = sets_list[0].copy()
    for s in sets_list[1:]:
        result = result ^ s
    return result
sets_list = [{1,2,3}, {2,3,4}, {3,4,5}]
print(multi_symmetric_difference(sets_list))