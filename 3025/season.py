"""season"""

month = int(input())
day = int(input())

skip = (day >= 21) and not month % 3

if month in [1, 2, 3]:
    if not skip:
        print("winter")
    else:
        print("spring")
elif month in [4, 5, 6]:
    if not skip:
        print("spring")
    else:
        print("summer")
elif month in [7, 8, 9]:
    if not skip:
        print("summer")
    else:
        print("fall")
elif month in [10, 11, 12]:
    if not skip:
        print("fall")
    else:
        print("winter")
