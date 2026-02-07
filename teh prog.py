#1
import string
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
#2
process = lambda s: " ".join(
    w[::-1]
    for w in s.split()
    if not any('0' <= c <= '9' for c in w) and len(w) % 2 == 0
)
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
#4
p = lambda s: " ".join(
    w.lower()
    for w in s.split()
    if sum(1 for c in w if c.isupper()) == 1
    and not w[0].isupper()
    and not w[-1].isupper()
)
print(p("helLo worLd PyThon TesT"))
#5
def compress_text(text):
    if not text:
        return ""
    result=[]
    count=1
    for i in range(1, len(text)+1):
        if i<len(text) and text[i].lower()==text[i-1].lower():
            count+=1
        else:
            result.append(text[i-count])
            if count>1:
                result.append(str(count))
            count=1
    return "".join(result)
print(compress_text("aaBbBcd"))
#6
c=lambda text: [
    word for word in text.split()
    if len(word)>=4
    and word.isalpha()
    and len(set(word.lower()))==len(word)
]
print(c("Apple orange car 1234 book"))
#7
def palindrome_words(text):
    cl=""
    for ch in text:
        if ch not in string.punctuation:
            cl+=ch
        else:
            cl+=" "
    words=cl.lower().split()
    palind=[]
    for word in words:
        if len(word)>=3 and word==word[::-1]:
            if word not in palind:
                palind.append(word)
    palind.sort()
    palind.sort(key=len, reverse=True)
    return palind
print(palindrome_words("азақ, шалаш, мадам, ана, аға, радар, қазақ."))
#8
vowels = "aeiouAEIOU"
process_text = lambda text: " ".join([
    word if any(char.isdigit() for char in word)
    else "VOWEL" if word[0] in vowels
    else "CONSONANT"
    for word in text.split()
])
print(process_text("Apple 2test banana Orange 123 sky"))
#9
def alternate_case_blocks(text, n):
    result=""
    for i in range(0, len(text), n):
        block = text[i:i+n]
        if (i//n)%2==0:
            result += block.upper()
        else:
            result += block.lower()
    return result
print(alternate_case_blocks("HelloWorldPython", 4))
#10
n= lambda text: len([
    word for word in text.split()
    if any(char.isdigit() for char in word)
    and not word[0].isdigit()
    and len(word)>=5
])
print(n("Python3 1abcde User42 Agent007"))
#11
def common_unique_chars(s1, s2):
    result=""
    for ch in s1:
        if ch in s2:
            if ch not in result:
                if not ch.isdigit():
                    if ch!=" ":
                        result += ch
    return result
print(common_unique_chars("hello 123", "gold 345"))
#12
v=lambda text: [
    w for w in text.split()
    if w[0].lower()==w[-1].lower()
    and w.lower()!=w.lower()[::-1]
    and len(w)>=3
]
print(v("almaty anna level area"))
#13
def replace_every_nth(text, n, char):
    result=""
