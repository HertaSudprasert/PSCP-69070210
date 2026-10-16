"""charm"""

num = int(input())
charm = []
pairs = []

for _ in range(0, num):
    charm.append(int(input()))

for i in charm:
    pairs.append(charm.count(i))

print(max(pairs))
