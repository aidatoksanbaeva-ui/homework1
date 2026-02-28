def analyze_strings_list(words):
    result = []
    for word in words:
        has_digit = False
        for char in word:
            if char >= '0' and char <= '9':
                has_digit = True
                break
        if has_digit:
            continue
        if len(word) % 2 == 0:
            new_word = word[::-1]
        else:
            new_word = ''
            for c in word:
                if 'a' <= c <= 'z':
                    new_word += chr(ord(c) - 32)
                else:
                    new_word += c
        if new_word not in result:
            result.append(new_word)
    return result
words = ["hello", "world", "test1", "python", "code", "HELLO"]
print(analyze_strings_list(words))