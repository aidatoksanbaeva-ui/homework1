def even_numbers(n):
    i=1
    while i<=n:
        if i%2==0:
            if i%4==0:
                yield "кратно 4"
            else:
                yield i
        i+=1
for i in even_numbers(10):
    print(i)