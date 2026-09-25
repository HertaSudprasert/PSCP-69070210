"""jarona"""

data = input()

L = int(data.split()[0])
N = int(data.split()[1])
num = 0

while ((num * L) * (num * L + 1) // 2) < N:
    num += 1

print(num)
