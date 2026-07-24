"""increase"""

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num2 - num1 > 0 and num3 - num2 > 0:
    print("increasing")
elif num2 - num1 < 0 and num3 - num2 < 0:
    print("decreasing")
else:
    print("neither")
