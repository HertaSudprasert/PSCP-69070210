"""saopan"""

l, n = map(int, input().split())
bridges = []

for _ in range(n):
    a, b = map(int, input().split())
    bridges.append((a, b))

max_bridges = 0

for k in range(l):
    current_count = 0
    for a, b in bridges:
        if a <= k and b >= k + 1:
            current_count += 1

    if current_count > max_bridges:
        max_bridges = current_count

print(max_bridges)
