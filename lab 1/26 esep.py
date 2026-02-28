def remove_duplicates_keep_last(nums):
    result = []
    for x in reversed(nums):
        if x not in result:
            result.append(x)
    result.reverse()
    return result
nums = [1, 2, 2, 3, 1, 4]
print(remove_duplicates_keep_last(nums))