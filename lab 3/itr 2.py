from functools import reduce
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
result=[reduce(lambda x,y: x*y,row) for row in matrix]
print(result)