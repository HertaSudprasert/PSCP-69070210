"""quardrant"""

x = int(input())
y = int(input())

#x == 0 and y == 0
if not x and not y:
    print("O")
else:
    pass

#x != 0 and y == 0
if not x and y:
    print("Y")
#x == 0 and y != 0
elif x and not y:
    print("X")
else:
    pass

if x > 0 and y > 0:
    print("Q1")
#x < 0 and y > 0
elif y > 0 > x:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
#x > 0 and y < 0
elif x > 0 > y:
    print("Q4")
