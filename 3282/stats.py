"""stats"""

num = int(input())

avg = 0
mini = None
maxi = None

for _ in range(0 , num):
    data = int(input())
    if mini is None:
        mini = data
    else:
        if data < mini:
            mini = data
    if maxi is None:
        maxi = data
    else:
        if data > maxi:
            maxi = data

    avg += data

avg = avg / num

print(f"MIN: {mini:.3f}")
print(f"MAX: {maxi:.3f}")
print(f"AVG: {avg:.3f}")
