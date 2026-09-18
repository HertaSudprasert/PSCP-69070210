"""arrow"""

k = int(input())
n = int(input())

center = n // 2

for i in range(n):
    thing = "*" * k
    far_from_center = abs(i - center)
    print(far_from_center)
