m_even=lambda a,b: [
    x for x, y in zip(a,b)
    if x==y and x%2==0
]
a=[4,2,7,6]
b=[4,2,9,6]
print(m_even(a,b))