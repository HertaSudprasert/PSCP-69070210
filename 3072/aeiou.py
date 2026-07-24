"""aeiou"""

text = input()

a = 0
e = 0
i = 0
o = 0
u = 0

for j in text:
    if j.lower() == "a":
        a += 1
    elif j.lower() == "e":
        e += 1
    elif j.lower() == "i":
        i += 1
    elif j.lower() == "o":
        o += 1
    elif j.lower() == "u":
        u += 1
    else:
        pass
if a:
    print(f"a : {a}")
if e:
    print(f"e : {e}")
if i:
    print(f"i : {i}")
if o:
    print(f"o : {o}")
if u:
    print(f"u : {u}")
