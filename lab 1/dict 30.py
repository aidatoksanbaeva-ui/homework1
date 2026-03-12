def partition_by_sum_parity(s):
    even_sum = set()
    odd_sum = set()
    for num in s:
        digit_sum = sum(int(d) for d in str(abs(num)))
        if digit_sum % 2 == 0:
            even_sum.add(num)
        else:
            odd_sum.add(num)
    return (even_sum, odd_sum)
s = {12, 23, 34, 45}
even_sum, odd_sum = partition_by_sum_parity(s)
print(even_sum)
print(odd_sum)