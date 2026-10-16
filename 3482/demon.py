"""help"""

demons = [
        ("Spider Demon", 1),
        ("Swamp Demon", 2),
        ("Arrow Demon", 1),
        ("Hand Demon", 2),
        ("Drum Demon", 3),
        ("Mugen Train", 2),
        ("Upper Moon", 3)
    ]

queue = list(demons)
killed_count = 0
total_attacks = 0

while killed_count < 5:
    name, num = queue.pop(0)
    print(name)
    attempts = 0
    killed = False

    while attempts < 2:
        guess = int(input())
        total_attacks += 1
        attempts += 1
        if guess == num:
            print("kill")
            killed_count += 1
            killed = True
            break
        if attempts == 2:
            print("back")
            break
    if not killed:
        queue.append((name, num))

print(total_attacks)
