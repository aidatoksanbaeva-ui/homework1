import math
def main():
#1
  nums = [2, 5, 7, 10]
  s = 0
  for num in nums:
      s += num

  print(s)
if __name__=='__main__':
    main()
#2
nums = [1, 2, 3, 4]
count = 0
for num in nums:
    if num%2==0:
        count += 1
print(count)

#3
nums = [2, 5, 6, 9]
max = nums[0]
min = nums[0]
for i in nums:
    if i>max:
        max = i
    elif i<min:
        min = i
print(max, min)

#4
nums = [-2, 5, -7, 10]
a = []
for i in nums:
    if i>0:
        a.append(i)
print(a)

#5
nums = [1, 2, 3, 4]
a=[]
for num in nums:
    nums=num**2
print(a)

#6
a = [1, 2]
b = [3, 4]
print(a+b)

#7
nums=[1, 2, 3, 4]
print(nums[::-1])

#8
nums=[1,2,2,3,2]
a=[]
x=2
for num in nums:
    if num!=x:
        a.append(num)
print(a)

#9
nums=[5,3,5,1,5]
index=[]
x=5
for i in range(len(nums)):
    if nums[i]==x:
        index.append(i)
print(index)

#10
nums=[1,2,3,4,5]
a=nums[::-1]
print(a)

#11
nums=[1,2,2,3,1,4]
a=[]
x=2
y=1
for num in nums:
    if num!=x and num!=y:
        a.append(num)
print(a)

#12
data=[[1,2],[3,4],[5,6]]
a=[]
for list in data:
    for num in list:
        a.append(num)
print(a)

#13
a=[1,3,5]
b=[2,4]
print(sorted(a+b))

#14
nums = [1, 2, 3, 4, 5]
k = 2
for i in range(k):
    l = nums.pop()
    nums.insert(0, l)
print(nums)
#15
nums =[5, 2, 8, 3, 1, 4]
jup=[]
tak=[]
for num in nums:
    if num%2==0:
        jup.append(num)
    else:
        tak.append(num)
result=jup+tak
print(result)
#16
