"""ddfff"""

num = int(input())

h = []

for _ in range(0, num):
    h.append(int(input()))

h.sort()
dist = 0

for i in range(0, num):
    multiplier = num - i
    dist += h[i] * multiplier

dist *= 2

print(dist)
