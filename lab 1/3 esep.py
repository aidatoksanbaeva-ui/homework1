#3
def top_k_words(text, k):
    text = text.lower()
    clean_text = ""
    for ch in text:
        if ch.isalpha() or ch == " ":
            clean_text += ch
    words = clean_text.split()
    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1
        else:
            freq[w] = 1
    unique_words = []
    for w in freq:
        unique_words.append(w)
    for i in range(len(unique_words)):
        for j in range(i + 1, len(unique_words)):
            if freq[unique_words[j]] > freq[unique_words[i]] or \
               (freq[unique_words[j]] == freq[unique_words[i]] and
                unique_words[j] < unique_words[i]):
                unique_words[i], unique_words[j] = unique_words[j], unique_words[i]
    return unique_words[:k]
text = "Apple banana apple orange banana apple pear orange"
print(top_k_words(text, 3))