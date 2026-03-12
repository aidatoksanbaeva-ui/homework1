f = lambda a, b: {x for x in a if x > (sum(b)/len(b)) and x not in b} if b else set()
a = {1, 5, 7, 9}
b = {2, 4, 6}
print(f(a, b))