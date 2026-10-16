"""bus stop"""

puukon = int(input())
num = int(input())

stations = {}

for _ in range(0, num):
    parts = list(map(int, input().split()))

    station_id = parts[0]
    people = parts[1:]
    stations[station_id] = people

bus = []
total_arrived = 0

for current_stop in range(1, num + 1):
    arrived_count = bus.count(current_stop)
    total_arrived += arrived_count
    bus = [d for d in bus if d != current_stop]

    if current_stop in stations:
        for dest in stations[current_stop]:
            if dest > current_stop and len(bus) < puukon:
                bus.append(dest)

print(total_arrived)
