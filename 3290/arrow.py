"""arrow"""

num1 = int(input())
num2 = int(input())

center = num2 // 2

for i in range(0, num2):
    print(" "*abs(i - center), "*" * num1, sep="")
