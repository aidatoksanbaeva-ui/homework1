from tasksss3 import count


def main():
   sett={"banan", "alma", 4, 5, 8}
   help(sett)
   print(sett)
if __name__ == '__main__':
    main()
    #3
students = {"aidos": 85,"bekzat": 90,"adil": 80,"dias": 95}
for i,j in sorted(students.items()):
    print(i,j)
    #4
dict={"aidos": 85,"bekzat": 90,"adil": 80,"dias": 95}
b=dict.values()
c=sorted(b)
print(c[-1]-c[0])
    #5
dict={"aidos": 81,"bekzat": 94,"adil": 78,"dias": 97}
b=dict.values()
jup=0
tak=0
for value in b:
    if value%2==0:
        jup+=1
    else:
        tak+=1
print("jup sandar sany:", jup)
print("tak sandar sany:", tak)
    #6
dict1={"a": 5, "b": 6, "c": 7, "d": 8}
dict2={}
for k,v in dict1.items():
    dict2[k]=dict1[k]
    dict2[k]=v*2
print(dict2)
    #7

     #1
set1={1,2,3,4,5}
set2={4,5,9,10,11}
dif=set1.difference(set2)
print(dif)
dif2=set2.difference(set1)
print(dif2)
sim=set1.symmetric_difference(set2)
print(sim)
     #2
A = {1, 2, 3, 4}
B = {4, 3, 2, 1}
if A == B:
    print("тен")
else:
    print("тен емес")
    #3
sett={5,8,6,7,9,10}
v=max(sett)
print("max:",v)
print("len:",len(sett))
    #4
a={1,2,3,4,5,6,7,8,9,10}
a=list(a)
for i in a:
    a=i**2
a=set(a)
print(a)
    #5
a = [43, 50, 60]
b = [40, 42, 51, 60, 61]
result = []
for size in a:
    count = 0
    for siz in b:
        if size - 1 <= siz <= size + 1:
            count += 1
    result.append(count)
print(result)

a = {1, 2, 3}
b = {3, 4, 5}
sett=a.intersection(b)
set1=a.union(b)
set2=a.difference(b)
print(set1)
print(set2)
print(sett)










