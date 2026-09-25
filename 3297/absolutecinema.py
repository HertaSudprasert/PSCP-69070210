"""absolute cinema"""

all_seats = int(input())

seat_list = []

while all_seats > 0:
    thing = input()

    age = int(thing.split()[0])
    ticket = int(thing.split()[1])

    if age < 15:
        seat_list.append(-1)
    elif ticket > all_seats:
        seat_list.append(-2)
    else:
        if 15 <= age <= 22:
            price = ticket * 120
        elif age >= 60:
            price = ticket * 75
        else:
            price = ticket * 150

        all_seats -= ticket
        seat_list.append(f"{price} {all_seats}")

for i in seat_list:
    print(i)
