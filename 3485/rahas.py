"""rahas"""

num = int(input())
raw = input().split()

seen = set()
sam = set()

for i in raw:
    num += 1
    if i in seen:
        sam.add(i)
    else:
        seen.add(i)

result = [i for i in raw if i not in sam]
result = sorted(set(result), key=int)

print(" ".join(result))
