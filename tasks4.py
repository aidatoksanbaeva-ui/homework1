import math
def main():
#1
  nums = [5, -2, 3, -7, 1]
  result = []
  for num in nums:
    result.append(num)
    if num < 0:
        result.append(0)
  print(result)
if __name__ == '__main__':
    main()
#2
nums=[4, 7, 4, 5, 4]
nums.pop(4)
nums.pop(0)
print(nums)
#3
t=(1,2,3,4,5)
x=6
t=t+(x, )
print(t)
#4
grades = [90, 75, 80, 100]сал
kosu=sum(grades)
count=len(grades)
orta=kosu/count
print(orta)
#5
nums = [2, 10, 4, 8, 6]
max = nums[0]
min = nums[0]
for i in nums:
    if i>max:
        max = i
    elif i<min:
        min = i
print(max, min)
print(max+min)
#6
a = [1, 2, 3, 4, 5, 6]
j=[]
t=[]
for i in a:
    if i%2==0:
        j.append(i)
    else:
        t.append(i)
print(j)
print(t)
#7
fruits = ['apple', 'banana', 'orange']
fruit=input("fruit: ")
if fruit in fruits:
    print("bar")
else:
    print("zhok")
#8
nums = (2, 4, 6, 8)
a=1
for num in nums:
    a=a*num
print(a)
#9
ages = (18, 22, 30, 17)
if ages in ages:
    ages < 18
print("Кәмелетке толмаған бар")
#10
data = (1, 5, 9)
a=0
for num in data:
    a=a+num
print(a)
if a>10:
    print("улкен")
else:
    print("киши")\
#11
t = (10, 20, 30)
nums = list(t)
nums.append(40)
print(nums)
#12
nums = [10, 2, 8, 15, 3]
maxx = nums[0]
minn = nums[0]
for i in nums:
    if i>maxx:
        maxx = i
    elif i<minn:
        minn = i
print(maxx-minn)
#13
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
#14
t = (10, 20, 30, 40)
for num in t:
    print(num)
#15
lst= [1, 2, 3, 4, "abc"]
nums = []
texts = []
lst.append("жүзім")
lst.append("құлпынай")
for x in lst:
    if type(x) == str:
        texts.append(x)
    else:
        nums.append(x)
print(lst)
print(nums)
print(texts)
print("Элемент саны:", len(lst))




