"""trash"""

num = int(input())

trash_machines = []

for _ in range(0, num):
    raw = map(float, input().split())
    raw = tuple(raw)
    trash_machines.append(raw)

for each_machines in trash_machines:
    over = False
    plastic = False
    can = False
    glass = False

    if sum(each_machines) > 50:
        over = True
    if each_machines[0] > 20:
        plastic = True
    if each_machines[1] > 20:
        can = True
    if each_machines[2] > 20:
        glass = True

    print(f"{sum(each_machines):.1f}", end="")
    if over:
        print(", Overloaded", end="")
    if plastic:
        print(", Check Type Plastic", end="")
    if can:
        print(", Check Type Can", end="")
    if glass:
        print(", Check Type Glass", end="")
    print()
