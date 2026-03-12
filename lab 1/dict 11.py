def group_by_length(words):
    result={}
    for word in words:
        l=len(word)
        if l not in result:
            result[l]=[]
        if word not in result[l]:
            result[l].append(word)
    return result
words=["cat", "dog", "apple", "car", "dog", "banana"]
print(group_by_length(words))