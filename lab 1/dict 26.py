def remove_elements_with_common_digits(s):
    digit_count = {}
    for num in s:
        for d in str(abs(num)):
            digit_count[d] = digit_count.get(d, 0) + 1
    result = set()
    for num in s:
        if all(digit_count[d] == 1 for d in str(abs(num))):
            result.add(num)
    return result
s = {12, 23, 34, 45, 56}
print(remove_elements_with_common_digits(s))