"""sorb"""

num1 = int(input())
num2 = int(input())
num3 = int(input())

sorb1 = num1 > 5
sorb2 = num2 > 20
sorb3 = num3 > 25

if sorb1 and sorb2 and sorb3:
    print("pass")
else:
    print("fail")
