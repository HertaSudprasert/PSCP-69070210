"""elo"""

RA = int(input())
RB = int(input())

win = input()

if win == "A":
    EA = 1 / (1 + 10 ** ((RB - RA) / 400))
    print(f"{EA:.2f}")
else:
    EB = 1 / (1 + 10 ** ((RA - RB) / 400))
    print(f"{EB:.2f}")
