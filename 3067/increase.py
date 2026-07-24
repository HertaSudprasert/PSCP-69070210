"""increase"""

num1 = float(input())
num2 = float(input())
num3 = float(input())

if num2 - num1 > 0 and num3 - num2 > 0:
    print("increasing")
elif num2 - num1 < 0 and num3 - num2 < 0:
    print("decreasing")
else:
    print("neither")
