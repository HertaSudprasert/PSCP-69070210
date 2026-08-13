"""https://www.desmos.com/calculator/qzom1fmi4p"""

rect1 = input()
rect2 = input()

Ax = int(rect1.split()[0])
Ay = int(rect1.split()[1])
Awidth = int(rect1.split()[2])
Aheight = int(rect1.split()[3])

Bx = int(rect2.split()[0])
By = int(rect2.split()[1])
Bwidth = int(rect2.split()[2])
Bheight = int(rect2.split()[3])

rectMaxX = max(Ax, Bx)
rectMaxY = max(Ay, By)

rectMinX = min(Ax + Awidth, Bx + Bwidth)
rectMinY = min(Ay + Aheight, By + Bheight)

width = max(rectMinX - rectMaxX, 0)
height = max(rectMinY - rectMaxY, 0)

area = width * height

if area:
    print(area)
else:
    print("no overlapping")
