def max_subarray_sum(nums, k):
    max_sum = None
    for i in range(len(nums) - k + 1):
        sub = nums[i:i + k]
        if all(x > 0 for x in sub):
            s = sum(sub)
            if max_sum is None or s > max_sum:
                max_sum = s
    return max_sum
nums = [1, 2, -3, 4, 5, 6, 0, 7]
k = 2
print(max_subarray_sum(nums, k))
