"""calc"""

num = int(input())

if num == 1:
    print(1)
else:
    calc = ""

    for i in range(1, num + 1):
        calc += str(i)
        calc += "+"
    print(len(calc))
    