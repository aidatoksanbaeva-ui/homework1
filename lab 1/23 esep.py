f = lambda nums: [
    nums[i] for i in range(len(nums))
    if i > 1
    and all(i % d != 0 for d in range(2, i))
    and nums[i] % 2 != 0
    and nums[i] > sum(nums) / len(nums)
]
nums = [1, 5, 7, 10, 3, 9, 12]
print(f(nums))