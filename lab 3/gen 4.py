def squares(n):
    i=1
    while i<=n:
        if i**2%2==0:
            yield "чётный квадрат"
        else:
            yield i**2
        i+=1
for x in squares(20):
    print(x)