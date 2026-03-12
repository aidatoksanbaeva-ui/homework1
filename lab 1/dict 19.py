def filter_by_digit_sum(nums):
    result = set()
    for num in nums:
        digit_sum = sum(int(d) for d in str(abs(num)))
        if digit_sum % 2 == 0 and num % 2 != 0:
            result.add(num)
    return result
nums = {13, 22, 35, 41, 123}
print(filter_by_digit_sum(nums))