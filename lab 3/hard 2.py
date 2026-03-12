words = ["кот", "машина", "арбуз", "дом", "ананас"]
result=[(lambda x: (x.upper() if len(word)>4 else "short") + ("*" if "а" in x else ""))(word) for word in words]
print(result)