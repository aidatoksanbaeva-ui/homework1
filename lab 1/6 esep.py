#6
c=lambda text: [
    word for word in text.split()
    if len(word)>=4
    and word.isalpha()
    and len(set(word.lower()))==len(word)
]
print(c("Apple orange car 1234 book"))