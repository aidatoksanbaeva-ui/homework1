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