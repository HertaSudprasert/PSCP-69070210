"""sahahkorn"""

from decimal import Decimal, ROUND_HALF_UP

samachick = input()
num = int(input())

total = Decimal("0")

for _ in range(0, num):
    total += Decimal(input())

if samachick == "Y":
    total = total - (total * Decimal("0.05"))
else:
    if total >= 500:
        total = total - (total * Decimal("0.03"))

totaldec = Decimal(total)
print(totaldec.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
