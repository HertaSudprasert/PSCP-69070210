"""taew"""

n, l = map(int, input().split())
h = list(map(int, input().split()))
a = list(map(int, input().split()))

prefix_max = [0] * n
current_max = 0

for i in range(n):
    current_max = max(current_max, h[i])
    prefix_max[i] = current_max

for i in range(l):
    target = a[i]
    idx = target - 1

    if not idx:
        print(0)
    else:
        max_in_front = prefix_max[idx - 1]
        required_height = max_in_front + 1
        chair_height = max(0, required_height - h[idx])
        print(chair_height)
