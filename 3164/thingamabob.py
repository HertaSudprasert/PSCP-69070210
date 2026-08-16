"""afagoighrieogjiaerogi"""

num = int(input())

pairs = []

for _ in range(0, num):
    first = int(input())
    second = int(input())
    pairs.append((first, second))

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

print(f'{"".join(thing)} = {sum(greater)}')
