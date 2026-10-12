"""sdgsdgsdg"""
import json

raw = input()

thing = json.loads(raw)

lek_ku = []

for i in thing:
    if not i % 2 or not i:
        lek_ku.append(i)

if not lek_ku:
    print("Nope")
else:
    for j in lek_ku:
        print(j)
