"""phrog"""

data = input()

jump_dist = int(data.split()[0])
target = int(data.split()[1])

dist = 0
jum_num = 0

while dist < target:
    if jump_dist > 0:
        dist += jump_dist
        jump_dist -= 2
        jum_num += 1
    else:
        break


if dist >= target:
    print(jum_num)
else:
    print(-1)
