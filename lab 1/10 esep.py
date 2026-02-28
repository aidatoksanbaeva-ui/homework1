#10
n= lambda text: len([
    word for word in text.split()
    if any('0'<=char<='9' for char in word)
    and not '0'<=word[0]<='9'
    and len(word)>=5
])
print(n("Python3 1abcde User42 Agent007"))