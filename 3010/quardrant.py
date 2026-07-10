"""quardrant"""

x = int(input())
y = int(input())


def quardrant(x: int, y: int):

    if x == 0 and y == 0:
        print("O")
        return

    if x == 0 and y != 0:
        print("Y")
        return
    elif x != 0 and y == 0:
        print("X")
        return

    if x > 1 and y > 1:
        print("Q1")
        return
    elif x < 1 and y > 1:
        print("Q2")
        return
    elif x < 1 and y < 1:
        print("Q3")
        return
    elif x > 1 and y < 1:
        print("Q4")
        return

quardrant(x, y)
 