#1
def analyze_text(text):
    text = text.lower()
    cleantext= ""
    for ch in text:
        if ('a' <=ch<= 'z') or ch==" ":
            cleantext += ch
    vowels="aeiouy"
    uniquevo=[]
    for ch in cleantext:
        if ch in vowels:
            if ch not in uniquevo:
                uniquevo.append(ch)
    words=cleantext.split()
    resultwords=[]
    for word in words:
        if len(word)>=5:
            if word[0]==word[-1]:
                if word[0] not in resultwords:
                    resultwords.append(word)
    return (len(uniquevo)," ".join(resultwords))
print(analyze_text("Hello, Anna went to level civic center!"))