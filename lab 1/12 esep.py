#12
v=lambda text: [
    w for w in text.split()
    if w[0].lower()==w[-1].lower()
    and w.lower()!=w.lower()[::-1]
    and len(w)>=3
]
print(v("almaty anna level area"))