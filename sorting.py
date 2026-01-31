#1
nums = [64, 34, 25, 12, 22, 11, 90]
def buble_sort(nums):
    l = len(nums)
    for i in range(l-1):
        for j in range(l-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    result = []
    for x in nums:
        result.append(x//2)
    return result
print(buble_sort(nums))
#1
def isascending(A):
    i = 1
    while i < len(A):
        if A[i] <= A[i - 1]:
            return "NO"
        i += 1
    return "YES"
A1 = [1, 7, 9]
print(isascending(A1))
#2
def max_last(A):
    max_value = A[0]
    last_max_index = 0
    for i in range(1, len(A)):
        if A[i] >= max_value:
            max_value = A[i]
            last_max_index = i
    return max_value, last_max_index
A2 = [1, 2, 1, 2, 1]
print(max_last(A2))
#3
counts = [0] * 9
x = int(input())
while x != 0:
    if 1 <= x <= 9:
        counts[x - 1] += 1
    x = int(input())
for c in counts:
    print(c)
#4
distances = [10, 20, 30]
prices = [50, 20, 30]
distances.sort()
#prices.sort(reverse=True)
total = 0
for i in range(len(distances)):
    total += distances[i] * prices[i]
print(total)
#5
arr = [1, 2, 3, -2, -4]
m = {}
i = 0
while i < len(arr):
    v = arr[i]
    if -v in m:
        print(m[-v], i)
        break
    m[v] = i
    i += 1
#6
S = 100
sizes = [100, 200, 50]
sizes.sort()
count = 0
total = 0
for x in sizes:
    if total +x <= S:
        total += x
        count += 1
print(count)
#7
def max_shoes(user_size, shoeses):
    shoes = []
    for s in shoeses:
        if s >= user_size:
            shoes.append(s)
    shoes.sort()
    count = 0
    last = user_size
    for s in shoes:
        if s >= last:
            count += 1
            last = s + 3
    return count
a=43
b=[40, 41, 52, 60, 61]
print(max_shoes(a, b))

#76
a = [43, 50, 60]
b = [40, 42, 51, 60, 61]
for size in a:
    l = [size -1, size +1]
    if size in b:
        l.append(size)
    count = 0
    for s in l:
        if s in b:
            count += 1
    print(count)




