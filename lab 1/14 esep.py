#14
f = lambda text: ",".join(
    w for w in text.split()
    if sum(1 for c in w if 'a' <= c.lower() <= 'z' and w.lower().count(c.lower()) == 1) > 3
    and all(w.lower().count(v) <= 1 for v in "aeiou")
)
print(f("apple orange banana sky fly"))
