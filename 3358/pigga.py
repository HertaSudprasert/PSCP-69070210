"""afagoighrieogjiaerogi"""

num = int(input())
raw = input().split()

pairs = []
for bruh in range(num):
    pairs.append((int(raw[2 * bruh]), int(raw[2 * bruh + 1])))

greater = []
for i in pairs:
    if i[0] > i[1]:
        greater.append(i[0])
    else:
        greater.append(i[1])

thing = []
for j in greater:
    thing.append(str(j))
    thing.append(" + ")

thing.pop()

if len(greater) == 1:
    print(greater[0])
else:
    print(f'{"".join(thing)} = {sum(greater)}')
