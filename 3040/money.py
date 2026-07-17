"""money"""

money = int(input())

rian_10 = money // 10
money -= rian_10 * 10

rian_5 = money // 5
money -= rian_5 * 5

rian_2 = money // 2
money -= rian_2 * 2

rian_1 = money // 1
money -= rian_1 * 1

print(f"10 = {rian_10}")
print(f"5 = {rian_5}")
print(f"2 = {rian_2}")
print(f"1 = {rian_1}")
