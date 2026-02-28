def flatten_and_filter(lst):
    result=[]
    spk=lst[:]
    while spk:
        x=spk.pop(0)
        if type(x)==list:
            spk+=x
        elif type(x)==int:
            if x>0 and x%4!=0:
                if x>10:
                    result.append(x)
    for i in range(len(result)):
        for j in range(i+1,len(result)):
            if result[i]>result[j]:
                result[i], result[j] = result[j], result[i]
    return result
n=[1,[12,[8,15],-20],25,[4,16,30]]
print(flatten_and_filter(n))
