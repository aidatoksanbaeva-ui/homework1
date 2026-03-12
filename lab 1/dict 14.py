def top_k_frequent(nums, k):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    items = list(freq.items())
    items.sort(key=lambda x: (-x[1], x[0]))
    top_k = items[:k]
    return {num for num, count in top_k}
nums = [4,1,2,2,3,3,3,4,4,4,5]
k = 3
print(top_k_frequent(nums, k))