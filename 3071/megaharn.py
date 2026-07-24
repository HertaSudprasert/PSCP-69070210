"""harn"""

A = int(input())
B = int(input())
d = int(input())
r = int(input())

N = []

for i in range(A, B + 1):
    if i % d == r:
        N.append(i)

print(len(N))
