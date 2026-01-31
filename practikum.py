#1
def search_elements():
    nums=[4,9,1,7,3,5]
    target=7
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1
print(search_elements())
#2
def binary_search():
    nums = [2, 5, 8, 12, 16, 23, 38, 56]
    target = 23
    first = 0
    last = len(nums)-1
    while first <= last:
        mid = (first+last)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            first = mid+1
        else:
            last = mid-1
    return -1
print(binary_search())
#3
def find_max():
    numss = [12, 99, 234, 7, 88, 42]
    max_value=numss[0]
    for num in numss:
        if num>max_value:
            max_value=num
    return max_value
print(find_max())
#4
def search_insert():
    nums = [1, 4, 6, 9, 15]
    target = int(input())
    first = 0
    last = len(nums) - 1
    while first <= last:
        mid = (first + last) // 2
        if nums[mid] == target:
            return f"{target} бар, индекс {mid}"
        elif nums[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    if first == 0:
        return f"{target} ({nums[0]}-дын алды)"
    elif first == len(nums):
        return f"{target} ({nums[-1]}-тын соны)"
    else:
        return f"индекс {first}, {nums[first-1]} мен {nums[first]} арасы"
print(search_insert())
#5
def linear_search():
    names = ["Alice", "Bob", "Charlie", "Diana", "Eva"]
    target = "Charlie"
    for i in range(len(names)):
        if names[i] == target:
            return i
    return -1
print(linear_search())
#6
def binary_search():
    words = ["apple", "banana", "carrot", "grape", "orange", "peach"]
    target = "orange"
    first = 0
    last = len(words) - 1
    while first <= last:
        mid = (first + last) // 2
        if words[mid] == target:
            return mid
        elif words[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return -1
print(binary_search())
#7
def binary_search(target):
    users = [
        {"id": 101, "name": "Alex"},
        {"id": 215, "name": "Max"},
        {"id": 340, "name": "Anna"},
        {"id": 540, "name": "Tim"}
    ]
    first = 0
    last = len(users) - 1
    while first <= last:
        mid = (first + last) // 2
        current = users[mid]["id"]
        if current == target:
            return users[mid]["name"]
        elif current < target:
            first = mid + 1
        else:
            last = mid - 1
    return "табылмады"
print(binary_search(340))
#8
nums = [2, 5, 9,12,13, 14, 20]
target = 14
def binary_search(nums, target):
    first = 0
    last = len(nums) - 1
    near = nums[0]
    while first <= last:
        middle = (first + last) // 2
        if abs(nums[middle] - target) < abs(near - target):
            near = nums[middle]
        if nums[middle] == target:
            return nums[middle]
        elif nums[middle] < target:
            first = middle + 1
        else:
            last = middle - 1
    return near
print(binary_search(nums, target))
#9
def adaptive_search(nums, target):
    if nums == sorted(nums):
        left= 0
        right=len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    else:
        for i, v in range(len(nums)):
            if v == target:
                return i
        return -1
nums = [1, 3, 8, 12, 20]
target = 12
print(adaptive_search(nums, target))

#234
nums = [2, 5, 9, 12, 13, 14, 20, 25, 30]
target = 14
def binary_search():
    first = 0
    last = len(nums) - 1
    while first <= last:
        mid = (first + last) // 2
        if nums[mid] == target:
            return nums[mid]
        elif nums[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return -1
juptar = []
taktar = []
for num in nums:
    if num > target:
        break
    if num % 2 == 0:
        juptar.append(num)
    else:
        taktar.append(num)
print("jup:", juptar)
print("tak:", taktar)