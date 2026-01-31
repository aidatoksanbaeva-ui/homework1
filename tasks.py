import math
#1
nums=[1,2,3,2,1]
sett=set(nums)
print(len(sett))
#2
set1= {1,3,2}
set2={4,3,2}
set3=set1 & set2
print(len(set3))
#3
a = "python"
b = "notebook"
s= set(a).intersection(set(b))
r=sorted(s)
print(r)
#4
mathh = {"Aida", "Nurlan", "Dana"}
cs = {"Dana", "Aruzhan"}
physics = {"Aida", "Serik"}
result=mathh.symmetric_difference(cs)
result=result.symmetric_difference(physics)
print(result)
#5
pythongr = {"Айгүл", "Бекзат", "Данияр"}
javagr = {"Айгүл", "Самат", "Лаура"}
gr = pythongr & javagr
python = pythongr - javagr
students = pythongr | javagr
print("тек еки курста окитын:", gr)
print("тек pythonда окитын:", python)
print("барлыгы:", students)
#6
data = [
    ("Ivanov", "paper"),
    ("Petrov", "pens"),
    ("Ivanov", "marker"),
    ("Ivanov", "paper"),
    ("Petrov", "envelope"),
    ("Ivanov", "envelope")
]
a={}
for k,v in data:
    if k not in a:
        a[k]=set()
    a[k].add(v)
for k,v in a.items():
    print(f"{k}: {', '.join(sorted(v))}")
#7
text = "Мен Python жақсы көремін және Python үйренемін"
a=text.split()
s={}
for i in a:
    if i in s:
        s[i]+=1
    else:
        s[i]=1
print(s)
#8
product={"alma": 300, "banan": 450, "sut": 550}
a=product.pop("banan")
product["potato"]=400
product["bread"]=200
product["airan"]=350
product["orange"]=500
product["meet"]=600
for k, v in product.items():
    if k in ["potato", "bread", "airan", "sut", "meet"]:
        product[k]*=1.3
    elif k in ["alma", "orange"]:
        product[k]*=1.2
print(product)
#9
students={"Aida":97, "Madi":50, "Alikhan":65, "Nargiz":70, "Aikyn":33}
a=max(students.values())
b=min(students.values())
s= sum(students.values()) / len(students)
print(a)
print(b)
print(s)\
#10
dict1 = {'alma': 10, 'banan': 5, 'nan': 3}
tauar=input("tauar=")
sany=int(input("sany="))
for k, v in dict1.items():
    if tauar==k and sany<v:
        print(tauar, "сатып алды,", "калды:", v-sany)
    elif tauar==k and sany>v:
        print("жеткиликсиз", "коймада", v, "гана бар")




