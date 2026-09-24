"""scheduel"""

carbs = int(input())
wela = int(input())

total_wela_sorn = carbs * wela

wela_sorn_hour = total_wela_sorn // 60
wela_sorn_minute = total_wela_sorn % 60

if wela_sorn_hour:
    print(f"{wela_sorn_hour} hours", end="")

if wela_sorn_hour and wela_sorn_minute:
    print(" ", end="")

if wela_sorn_minute:
    print(f"{wela_sorn_minute} minute")

if not wela_sorn_hour and not wela_sorn_minute:
    print("No teaching")
