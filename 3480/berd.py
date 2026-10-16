"""berd"""

num = int(input())

trees = list(map(int, input().split()))
c = 0

for i in range(0, num):
    left = trees[i - 1] if i - 1 >= 0 else 0
    right = trees[i + 1] if i + 1 < num else 0

    if right < trees[i] > left:
        c += 1

print(c)
