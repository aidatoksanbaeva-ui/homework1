def group_by_parity_and_sort(nums):
    even=[]
    odd=[]
    for x in nums:
        if x%2==0:
            even.append(x)
        else:
            odd.append(x)
    for i in range(len(even)):
        for j in range(i + 1, len(even)):
            if even[i] > even[j]:
                even[i], even[j] = even[j], even[i]
    for i in range(len(odd)):
        for j in range(i + 1, len(odd)):
            if odd[i] > odd[j]:
                odd[i], odd[j] = odd[j], odd[i]
    return even + odd
nums = [7, 2, 5, 8, 1, 4]
print(group_by_parity_and_sort(nums))