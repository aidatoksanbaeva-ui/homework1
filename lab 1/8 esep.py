#8
vowels = "aeiouAEIOU"
process_text = lambda text: " ".join([
    word if any('0'<=char<='9' for char in word)
    else "VOWEL" if word[0] in vowels
    else "CONSONANT"
    for word in text.split()
])
print(process_text("Apple 2test banana Orange 123 sky"))