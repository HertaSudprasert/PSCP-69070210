"""even odd"""


num1 = int(input())
num2 = int(input())
num3 = int(input())

even = 0
odd = 0

if not num1 % 2:
    even += 1
else:
    odd += 1

if not num3 % 2:
    even += 1
else:
    odd += 1

if not num2 % 2:
    even += 1
else:
    odd += 1

print(even)
print(odd)
