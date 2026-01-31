#1
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
#2
def fact2(n):
    if n<2:
        return n
    else:
        return n*fact2(n-2)
print(fact2(5))
#3
def fib(n):
    if n<=3:
        return 1
    else:
        return fib(n-3)+fib(n-2)+fib(n-1)
print(fib(6))
#4
def palindrom(s):
    if len(s)<=1:
        return True
    if s[0] != s[-1]:
         return False

    return palindrom(s[1:-1])
print(palindrom("ala"))
#5
def air(n):
    if len(n)<=1:
        return n
    return n[0]+"("+air(n[1:-1])+")"+n[-1]
print(air("class"))
#6
def sun(n):
    if n == 0:
        return 0
    return n%10+sun(n//10)
print(sun(1467))
#1
def darezhe(n):
    if n == 1:
        return True
    if n == 0 or n % 2 != 0:
        return False
    return darezhe(n // 2)
n = int(input("san:"))
print("YES" if darezhe(n) else "NO")
#2
def fakt(n, i=2):
    if n == 1:
        return n
    if n % i == 0:
        print(i, end=' ')
        fakt(n // i, i)
    else:
        fakt(n, i + 1)
n = int(input("san:"))
fakt(n)
#3
def nums(n, k=1, c=0):
    if n == 0:
        return
    print(k, end=' ')
    c += 1
    if c == k:
        k += 1
        c = 0
    nums(n-1, k, c)
n = int(input("san:"))
nums(n)
#4
def rev(n, r=0):
    if n == 0:
        return r
    return rev(n // 10, r * 10 + n % 10)
n = int(input("san:"))
print(rev(n))
#5
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
a = int(input("first san: "))
b = int(input("second san: "))
print("LCM:", lcm(a, b))



