"""dadada"""
num = input().split()
X1 = int(num[0])
Y1 = int(num[1])
X2 = int(num[2])
Y2 = int(num[3])

counter = float("inf")

for A in range(X2, Y2 + 1):
    forza = (X1 // A) * Y1

    remaining_width = X1 % A
    vertical = remaining_width * (Y1 // A)

    total = forza + vertical
    used = total * A
    wasted_space = (X1 * Y1) - used

    if wasted_space < counter:
        counter = wasted_space

print(counter)
