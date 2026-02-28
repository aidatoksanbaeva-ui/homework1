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