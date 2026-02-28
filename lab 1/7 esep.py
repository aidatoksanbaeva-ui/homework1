#7
def palindrome_words(t):
    t = t.lower()
    s = ""
    for c in t:
        if 'a'<=c<='z' or c==" ":
            s += c
    w = s.split()
    p = []
    for x in w:
        if len(x)>=3:
            r=""
            for i in range(len(x) - 1, -1, -1):
                r += x[i]
            if x == r and x not in p:
                p.append(x)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if len(p[j])>len(p[i]) or \
               (len(p[j]) == len(p[i]) and p[j] < p[i]):
                p[i], p[j] = p[j], p[i]
    return p
print(palindrome_words("Level, radar! civic stats noon deed apple"))