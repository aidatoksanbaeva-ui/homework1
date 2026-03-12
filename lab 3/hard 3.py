def process_numbers(numbers):
    gen = (n for n in numbers)
    positive = filter(lambda x: x >= 0, gen)
    transformed = map(lambda x: x / 2 if x % 2 == 0 else x*3 + 1, positive)
    for num in transformed:
        yield num
numbers = [5, -2, 8, 0, -7, 3]
for x in process_numbers(numbers):
    print(x)
