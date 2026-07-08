"""power"""


from decimal import Decimal, getcontext

expo = int(input())

getcontext().Emax = 200000000000000000
result = Decimal("7") ** Decimal(f"{expo}")

print(str(result))
print(str(result).split('E', maxsplit=1)[0][-1])
