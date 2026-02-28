filter_set = lambda s: {
    x for x in s
    if x > (sum(s) / len(s))
    and x % 2 != 0
    and x % 5 != 0
}
nums = {3, 7, 10, 15, 21, 8}
print(filter_set(nums))