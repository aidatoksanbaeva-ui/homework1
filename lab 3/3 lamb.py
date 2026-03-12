numbers = [5, 12, 7, 20, 33, 8]
evens=list(filter(lambda x: x%2==0 and x>10, numbers))
print(evens)