"""sinka"""

nnn = int(input())

stock = []

for _ in range(0, nnn):
    thing = int(input())
    stock.append(thing)

SUM = 0
EVEN = 0
ODD = 0
for i in stock:
    if not i % 2:
        EVEN += 1
    else:
        ODD += 1
    SUM += i

print(f"SUM {SUM}")
print(f"EVEN {EVEN}")
print(f"ODD {ODD}")
