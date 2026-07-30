"""birthday"""

from datetime import date

y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())

guy1 = date(y1, m1, d1)
guy2 = date(y2, m2, d2)

diff = guy2 - guy1

if abs(diff.days) <= 7:
    print(0)
elif diff.days > 0:
    print(1)
else:
    print(2)
