"""toopel"""

raw = input().split()
num = input()

toopel = tuple(raw)

side = toopel.count(num)
inside = toopel.index(num)

for _ in range(0, side):
    print(((str(inside) + " ") * side).strip())
