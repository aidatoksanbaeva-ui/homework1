f = lambda lists: [
    sum(inner) / len(inner)
    for inner in lists
    if len(inner) >= 3 and sum(inner) % 2 == 0
]
lists=[
    [7, 2, 5, 8, 1, 4],
    [7, 2, 5, 8, 1, 9], ]
print(f(lists))