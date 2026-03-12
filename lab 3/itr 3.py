words = ["кот", "машина", "ананас", "дом"]
result=[n for n in words if len(n)>4 and "а" not in n]
print(result)