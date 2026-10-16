"""bus"""

row = int(input())
col = int(input())
seat = int(input())

for i in range(row, 0, -1):
    line = ""
    for j in range(col):
        if line:
            line += " "
        n = i + j * row
        if n > 99:
            continue
        line += f"{n:02d}" if n != seat else "XX"
    print(line)
    if i != 1 and not (i-1) % 2:
        print("")
