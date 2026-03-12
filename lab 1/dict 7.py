a={1, 2, 3, 4}
b={3, 4, 5, 6}
f=lambda a,b:{x for x in (a^b)if x%2==0}
print(f(a,b))