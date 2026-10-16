"""light"""

num = int(input())

rail = [False] * 360
for _ in range(0, num):
    a, b = map(int, input().split())
    current = a

    while current != b:
        rail[current] = True
        current = (current + 1) % 360

if all(rail):
    print(360)
else:


    ext_rail = rail + rail
    max_len = 0
    current_len = 0

    for val in ext_rail:
        if val:
            current_len += 1
            if current_len > max_len:
                max_len = current_len
        else:
            current_len = 0

    if max_len > 360:
        max_len = 360
    print(max_len)
