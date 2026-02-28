#4
p = lambda s: " ".join(
    w.lower()
    for w in s.split()
    if sum(1 for c in w if c.isupper()) == 1
    and not w[0].isupper()
    and not w[-1].isupper()
)
print(p("helLo worLd PyThon TesT"))