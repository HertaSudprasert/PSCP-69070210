"""car"""

num = int(input())
p = []
v = []

for _ in range(0, num):
    pi, vi = map(int, input().split())
    p.append(pi)
    v.append(vi)

p.reverse()
v.reverse()

data = list(zip(p, v))
max_v = data[0][1]
no_sale = 0

for _, vi in data:
    if vi < max_v:
        no_sale += 1
    else:
        max_v = vi

print(no_sale)
