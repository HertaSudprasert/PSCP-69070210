"""space"""


import math

initial = input()
final = input()

x1 = int(initial.split()[0])
y1 = int(initial.split()[1])
z1 = int(initial.split()[2])

x2 = int(final.split()[0])
y2 = int(final.split()[1])
z2 = int(final.split()[2])

distance = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2))

print(f"{distance:.2f}")
