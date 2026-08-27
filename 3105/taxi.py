"""taxi"""

dist = int(input())

raka = 35

for i in range(1, dist):
    if i < 10:
        raka += 5
    else:
        raka += 8

if not dist:
    raka = 0
print(raka)
