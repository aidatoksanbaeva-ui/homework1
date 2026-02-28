def deep_sum(d):
    total=0
    for v in d.values():
        if '0'<=v<='9':
            total += v
        else:
            for i in v:
                if 'a'<=i<='z':
                    total += i
    else:
        total+=deep_sum(v)
    return total


