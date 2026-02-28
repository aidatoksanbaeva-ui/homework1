#16
def transform_list(nums):
    result = []
    for n in nums:
        if n < 0:
            continue
        if n % 2 == 0:
            result.append(n * n)
        elif n > 10:
            s = 0
            temp = n
            while temp > 0:
                s += temp % 10
                temp = temp // 10
            result.append(s)
        else:
            result.append(n)
    return result
print(transform_list([4, -5, 13, 9, 12, -2, 7, 22]))
