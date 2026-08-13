"""ink"""

import math

PI = 3.1416

set1 = input()

area_expand = int(set1.split()[0])
people = int(set1.split()[1])

house = []

while people > 0:
    housepos = input()

    x = int(housepos.split()[0])
    y = int(housepos.split()[1])

    house.append((x, y))
    people -= 1

time = 0
for houses in house:
    dist = (houses[0] ** 2) + (houses[1] ** 2)
    time += math.ceil((dist / area_expand) * PI) - time
    print(time)
