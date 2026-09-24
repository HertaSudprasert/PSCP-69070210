"""arrow"""

direction = input()
num = int(input())

def make_arrow(direct: str, thicc: int):
    """makes aeerow"""
    if direct == "L":
        for i in range(1, (thicc * 2)):
            stars = abs(thicc - i)
            print(" " * stars, "*" * (stars + 1), sep="")
    elif direct == "R":
        for i in range(1, (thicc * 2)):
            stars = abs(thicc - i)
            space = (thicc * 2) - stars
            print(" " * ((space - thicc - 1) * 2), "*" * (stars + 1), sep="")

for sides in direction:
    make_arrow(sides, num)
    if len(direction) != 1:
        print()
