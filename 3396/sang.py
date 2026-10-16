"""sgsdgsdg"""
n, k = map(int, input().split())

records = []

for _ in range(n):
    records.append(int(input()))

fastest = min(records)
win = 0

for t in records:
    if k * fastest > (k - 1) * t:
        win += 1

print(win)
