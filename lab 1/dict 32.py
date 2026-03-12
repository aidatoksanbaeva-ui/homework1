def pairwise_intersections(sets_list):
    if len(sets_list) < 2:
        return []
    result = []
    for i in range(len(sets_list) - 1):
        result.append(sets_list[i] & sets_list[i+1])
    return result
sets_list = [{1,2,3}, {2,3,4}, {3,4,5}]
print(pairwise_intersections(sets_list))