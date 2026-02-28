f = lambda a, b: [x for x in a if x not in b and x > sum(a)/len(a)]
a = [1, 5, 8, 3, 10]
b = [3, 8]
print(f(a, b))
