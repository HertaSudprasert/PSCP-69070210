"""fffff"""
def get_infection_chance(x1, y1, l): #x, y, infected
    """chance of infect"""
    chance = 0

    for p in l:
        if x1 == p[0] and y1 == p[1]:
            chance = 100
            break
        if abs(x1 - p[0]) <= 1 and abs(y1 - p[1]) <= 1:
            chance = max(chance, 60)
        if abs(x1 - p[0]) <= 2 and abs(y1 - p[1]) <= 2:
            chance = max(chance, 20)

    return chance


row, column = map(int, input().split())
r1, r2 = map(int, input().split())
infected = []

for _ in range(int(input())):
    infected.append(list(map(int, input().split())))

rabbit_chance = 0
safe_zones = 0

for x in range(row):
    for y in range(column):
        c = get_infection_chance(x, y, infected)
        if not c:
            safe_zones += 1
        if x == r1 and y == r2:
            rabbit_chance = c

print(safe_zones)
print(f"{rabbit_chance}%")
