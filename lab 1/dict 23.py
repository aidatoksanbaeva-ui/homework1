def group_by_last_letter(words):
    result = {}
    for word in words:
        if not word:
            continue
        last = word[-1]
        if last not in result:
            result[last] = []
        if word not in result[last]:
            result[last].append(word)
    return result
words = ["apple", "banana", "grape", "peach", "orange", "apricot"]
print(group_by_last_letter(words))