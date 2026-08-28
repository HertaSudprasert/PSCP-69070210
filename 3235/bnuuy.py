"""bnuuy"""

num = int(input())

hzahehgeGEGHEghEOGH = []
negjwegegekgegeg = []

for _ in range(0, num):
    data = input()

    bnuuy_name = data.split()[0]
    bnuuy_weight = int(data.split()[1])

    hzahehgeGEGHEghEOGH.append(bnuuy_name)
    negjwegegekgegeg.append(bnuuy_weight)

fat_counter = 0
fattest = max(negjwegegekgegeg)

for abababasbf in negjwegegekgegeg:
    if abababasbf > 15:
        fat_counter += 1

print(fat_counter)
print(hzahehgeGEGHEghEOGH[negjwegegekgegeg.index(fattest)])
