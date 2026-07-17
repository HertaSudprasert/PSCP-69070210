"""calc"""

num = int(input())

if num == 1:
    print(1)
else:
    calc = 0

    for i in range(1, num + 1):
        calc += len(str(i))
        calc += 1
    print(calc)
