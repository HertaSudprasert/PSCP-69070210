"""arrow"""

k = int(input())
n = int(input())

center = n // 2

for i in range(n):
    thing = "*" * k
    far_from_center = abs(center - i)
    spaces = center - far_from_center
    print(" " * spaces, thing, sep="")
