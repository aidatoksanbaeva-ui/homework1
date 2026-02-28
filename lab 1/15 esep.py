#15
def word_pattern_sort(text):
    vowels = "aeiouAEIOU"
    words = text.split()
    groups = {}
    for w in words:
        l = 0
        for _ in w:
            l += 1
        if l not in groups:
            groups[l] = []
        groups[l].append(w)
    result = []
    lengths = []
    for l in groups:
        lengths.append(l)
    for i in range(len(lengths)):
        for j in range(i+1, len(lengths)):
            if lengths[i] > lengths[j]:
                lengths[i], lengths[j] = lengths[j], lengths[i]
    for l in lengths:
        group = groups[l]
        for i in range(len(group)):
            for j in range(i+1, len(group)):
                count_i = 0
                count_j = 0
                for c in group[i]:
                    for v in vowels:
                        if c == v:
                            count_i += 1
                for c in group[j]:
                    for v in vowels:
                        if c == v:
                            count_j += 1
                if count_j > count_i or (count_j == count_i and group[j] < group[i]):
                    group[i], group[j] = group[j], group[i]
        for w in group:
            result.append(w)
    return result
print(word_pattern_sort("apple banana cat dog eagle igloo"))