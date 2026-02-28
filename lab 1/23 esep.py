f = lambda nums: [
    nums[i] for i in range(len(nums))
    if i > 1
    and all(i % d != 0 for d in range(2, i))
    and nums[i] % 2 != 0
    and nums[i] > sum(nums) / len(nums)
]