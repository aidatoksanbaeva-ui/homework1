numbers = [1, 2, 3, 4, 5, 6]
result=list(map(lambda x: x**2 if x%2==0 else x*3, numbers))
print(result)