#1
from art import *
Art = text2art("LAB", font='block', chr_ignore=True)
print(Art)
#2
print(text2art("Zhansaya", space=1))
#3
tprint("67",font="rnd-large")
#4
tprint("Aida","rnd-xlarge")
#5
with open('korgau.rtf') as f:
    s = f.read()
    print(len(s), repr(s[:20]), repr(s[-20:]))




