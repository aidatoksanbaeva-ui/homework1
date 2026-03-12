def sorted_unique_chars(strings):
    chars = set()
    for s in strings:
        for c in s:
            if not c.isdigit() and c != ' ':
                chars.add(c)
    return sorted(chars)
strings = ["hello world", "python 3", "chatgpt"]
print(sorted_unique_chars(strings))