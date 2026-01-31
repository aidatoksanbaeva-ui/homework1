#1
def num(n):
    print(f"2 дәрежесі: {n**2}")
    print(f"3 дәрежесі: {n**3}")
    print(f"4 дәрежесі: {n**4}")
    print(f"5 дәрежесі: {n**5}")
    print(f"6 дәрежесі: {n**6}")
print(num(2))
#2
def nums():
    for i in range(3,16):
        if i%2!=0:
            print(i**2)
nums()
#3
def numm():
    for i in range(10,25):
        if i%3!=0:
            a=i**0.5
            print(a)
numm()
#4
def sanau(nums):
    tak=0
    jup=0
    for num in nums:
        if num%2==0:
            jup+=1
        else:
            tak+=1
    print(tak)
    print(jup)
numbers=[1,2,3,4,5,6]
sanau(numbers)
#5
def c_to_f (c):
 return (c*9/5)+32
print(c_to_f(77))
print(c_to_f(95))
print(c_to_f(50))

#29
text=input()
result=""
for i in text:
    if i.isdigit():
        result=i*2
    else:
        result += i
print(result)

#1
def analyze_text(text):
    text = text.lower()
    clean_text = ""
    for ch in text:
        if ch.isalpha() or ch == " ":
            clean_text += ch
    vowels = "aeiouy"
    unique_vowels = []
    for ch in clean_text:
        if ch in vowels:
            if ch not in unique_vowels:
                unique_vowels.append(ch)
    words = clean_text.split()
    result_words = []
    for word in words:
        if len(word) >= 5:
            if word[0] == word[-1]:
                if word not in result_words:
                    result_words.append(word)
    return (len(unique_vowels), " ".join(result_words))
text = "Hello, Anna went to level civic center!"
print(analyze_text(text))






