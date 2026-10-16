"""fasfas"""

num = int(input())
shots = []

for _ in range(0, num):
    raw = input()

    x = int(raw.split()[0])
    y = int(raw.split()[1])
    d = int(raw.split()[2])
    shots.append((x, y, d))

for tx in range(0, 1001):
    for ty in range(0, 1001):
        vaild = True
        for x, y, d in shots:
            if (x - tx) ** 2 + (y - ty) ** 2 != d ** 2:
                vaild = False
                break
        if vaild:
            print(f"{tx} {ty}")
