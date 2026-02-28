#13
def replace_every_nth(text, n, char):
    result = ""
    i = 0
    while i < len(text):
        if text[i] == " " or ('0' <= text[i] <= '9'):
            result += text[i]
        else:
            start = i
            while i < len(text) and text[i] != " ":
                i += 1
            word_len = i - start
            if word_len < 3:
                result += text[start:i]
            else:
                for j in range(start, i):
                    if (j - start + 1) % n == 0:
                        result += char
                    else:
                        result += text[j]
            continue
        i += 1
    return result
print(replace_every_nth("Hello world 123 hi", 2, "*"))
