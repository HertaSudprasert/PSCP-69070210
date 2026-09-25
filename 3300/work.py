"""work"""

num = int(input())

early = 0
ot = 0


for _ in range(0, num):
    thing = int(input())

    if thing <= 18:
        early += 1
    else:
        ot += 1

print(num + max(0, ot - 1 - early))
