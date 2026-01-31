def main():
 #1
    nums = int(input("enter numbers: "))
    s = 0
    for i in range (1,nums+1):
        if i%2 != 0:
            s = s+(i ** 2)
    print(s)
if __name__ == '__main__':
    main()
#2
a=int(input("Enter a number: "))
t=a
r=0
while a > 0:
    digit = a % 10
    r=r*10+digit
    a = a // 10
if r==t:
    print("polidrom")
else:
    print("don't polidrom")
#3
n=int(input("Enter a number: "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
print(count)
#4
n = int(input("n= "))
t = 1
found = False
while n > 0:
    num = n%10
    if num%2!=0:
        t =t*num
        found = True
    n =n//10
if found:
    print("Так цифрлардын кобейтиндиси :", t)
else:
    print(0)
#5
t = 0
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    t += num
print("Қосынды:", t)
#6
n = int(input("1-сан: "))
ulken=n
kishi=n
for i in range(n - 1):
    num = int(input(f"{i+2}-сан: "))
    if num < kishi:
        kishi = num
    if num > ulken:
        ulken = num
print("kishi:", kishi)
print("ulken:", ulken)
#7
summa = 0
n = 0
while summa <= 100:
    n += 1
    summa += n
print("summa:", summa)
print("n=:", n)
#8
t = input("Enter text: ")
s = input("Enter symbol: ")
c = 0
for x in t:
    if x == s:
        c += 1
print(f' {s} = {c} ')
#9
n = int(input("Enter a number: "))
t=0
for i in range(1,n+1):
    t=t+i
    print(i, end=", ")
print(t)
#10
n = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")







