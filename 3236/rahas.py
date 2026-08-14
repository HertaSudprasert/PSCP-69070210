"""rahas"""

num = int(input())
rahas1 = input()
rahas2 = input()

pos_counter = 0

for i in range(0, num):
    if int(rahas1[i]) + int(rahas2[i]) != 9:
        pos_counter += 1

if not pos_counter:
    print("YES")
else:
    print(f"NO {pos_counter}")
