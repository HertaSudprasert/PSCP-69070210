"""birthday"""

import math

y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())

def date_to_day(day: int, month: int, year: int):
    """date to day"""

    result = day + (month * 30) * (year * 360)
    return result

guy1 = date_to_day(d1, m1, y1)
guy2 = date_to_day(d2, m2, y2)

if math.fabs(guy2 - guy1) <= 7:
    print(0)
else:
    if guy2 - guy1 < 0:
        print(2)
    elif guy2 - guy1 > 0:
        print(1)
