def longest_increasing_sublist(nums):
    if not nums:
        return []
    longest = []
    current = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current.append(nums[i])
        else:
            if len(current)>len(longest):
                longest = current
            current = [nums[i]]
    if len(current) > len(longest):
        longest = current
    return longest
nums = [1, 2, 3, 2, 5, 6, 7, 1]
print(longest_increasing_sublist(nums))