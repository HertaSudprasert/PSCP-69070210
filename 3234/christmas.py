"""christmas"""

data = input()

color = data.split()[0]
num = int(data.split()[1])

if color == "R":
    col_index = 0
elif color == "G":
    col_index = 1
else:
    col_index = 2

coler = ["Red", "Green", "Blue"]

for _ in range(0, num):
    if col_index > 2:
        col_index = 0
    print(coler[col_index], end=" ")

    col_index += 1
