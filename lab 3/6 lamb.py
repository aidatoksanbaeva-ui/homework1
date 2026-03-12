numbers = [0, -3, 5, -7, 8]
result=list(map(lambda x: "положительное" if x>0 else "отрицательное" if x<0 else "ноль", numbers))
print(result)