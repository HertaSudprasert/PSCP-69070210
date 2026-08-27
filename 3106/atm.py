"""ATM"""

money = int(input())

neungpan = 0
haroi = 0
neungroi = 0

if (money < 100) or (money > 20000):
    print("ERROR")
else:

    neungpan = money // 1000
    money -= neungpan * 1000

    haroi = money // 500
    money -= haroi * 500

    neungroi = money // 100
    money -= haroi * 100

    if money % 100:
        print("ERROR")
    else:

        if neungpan:
            print(f"1000 = {neungpan}")

        if haroi:
            print(f"500 = {haroi}")

        if neungroi:
            print(f"100 = {neungroi}")
