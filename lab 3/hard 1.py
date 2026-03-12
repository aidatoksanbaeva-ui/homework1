def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
def special_numbers(n):
    i=1
    while i<=n:
        if i%3==0 and i%5==0:
            yield "FizzBuzz"
        elif i%5==0:
            yield "Buzz"
        elif i%3==0:
            yield "Fizz"
        elif is_prime(i):
            yield "простое"
        else:
            yield i
        i+=1
for x in special_numbers(15):
    print(x)