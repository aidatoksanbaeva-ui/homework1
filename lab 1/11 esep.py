#11
def common_unique_chars(s1, s2):
    result=""
    for ch in s1:
        if ch in s2:
            if ch not in result:
                if not '0'<=ch<='9':
                    if ch!=" ":
                        result += ch
    return result
print(common_unique_chars("hello 123", "gold 345"))