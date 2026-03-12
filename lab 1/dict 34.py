def top_k_smallest_unique(nums, k):
    unique_nums = set(nums)
    sorted_nums = sorted(unique_nums)
    return set(sorted_nums[:k])
nums = [5, 3, 1, 2, 3, 4, 1]
k = 3
print(top_k_smallest_unique(nums, k))