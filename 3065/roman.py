"""roman"""

num = int(input())

roman = [
    "I",
    "II",
    "III",
    "IV",
    "V",
    "VI",
    "VII",
    "VIII",
    "IX",
]

if 0 < num < 10:
    print(roman[num - 1])
elif num < 0:
    print("Error : Please input positive number")
elif not num or num > 9:
    print("Error : Out of range")
