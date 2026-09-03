"""circl"""

data = input()

N = int(data.split()[0])
K = int(data.split()[1])
T = int(data.split()[2])

people_count = 0
gift_pos = 1

while True:
    people_count += 1

    if gift_pos == T:
        break

    next_person = (gift_pos - 1 + K) % N + 1

    if next_person == 1:
        break

    gift_pos = next_person

print(people_count)
