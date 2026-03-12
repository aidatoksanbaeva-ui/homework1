def matrix_transform(matrix):
    for row in matrix:
        for x in row:
            yield (
                "кратно 6" if x % 6 == 0
                else "чётное" if x % 2 == 0
                else "кратно 3" if x % 3 == 0
                else x
            )
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for x in matrix_transform(matrix):
    print(x)