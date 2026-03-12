vowels = set("aeiouAEIOU")
f = lambda d: [k for k, v in sorted(d.items(), key=lambda x: (sum(1 for c in x[0] if c in vowels), -x[1]))]
d = {
    "apple": 5,
    "banana": 3,
    "cat": 7,
    "door": 4,
    "elephant": 2
}
print(f(d))