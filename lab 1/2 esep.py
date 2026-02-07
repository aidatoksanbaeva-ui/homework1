#2
process = lambda s: " ".join(
    w[::-1]
    for w in s.split()
    if not any('0' <= c <= '9' for c in w) and len(w) % 2 == 0
)
