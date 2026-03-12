def common_elements_all(sets_list):
    if not sets_list:
        return set()
    result = sets_list[0]
    for s in sets_list:
        result = result & s
    return result
sets_list = [
    {1,2,3,4},
    {2,3,5},
    {0,2,3,8}
]
print(common_elements_all(sets_list))