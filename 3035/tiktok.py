"""ar tiktok"""

import math

inputset = input()

radius = float(inputset.split()[0])
x = float(inputset.split()[1])
y = float(inputset.split()[2])

dist = math.sqrt((x ** 2) + (y ** 2))

if dist < radius:
    print("IN")
elif dist == radius:
    print("ON")
else:
    print("OUT")
