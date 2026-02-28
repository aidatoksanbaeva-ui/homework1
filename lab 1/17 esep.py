count_digits = lambda n: 1 if -10 < n < 10 else 1 + count_digits(n // 10)
result = lambda nums: [
    x**2
    for x in nums
    if (x % 3 == 0 or x % 5 == 0)
    and x % 15 != 0
    and count_digits(x) % 2 == 1
]
nums = [3, 5, 9, 10, 15, 25, 111, 1005, 30]
print(result(nums))