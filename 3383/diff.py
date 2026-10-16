"""fafasf"""
n = int(input())
m = int(input())
listy = []
grupa = []
grupb = []

for _ in range(n):
    grupa.append(int(input()))

for _ in range(m):
    grupb.append(int(input()))

for i in grupa:
    if i not in grupb and i not in listy:
        listy.append(i)

listy.sort()
print(*listy)
