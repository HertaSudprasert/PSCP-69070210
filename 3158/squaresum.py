"""square sum"""

num = int(input())

num_thing = []

for i in range(1, num + 1):
    num_thing.append(i ** 2)

print(sum(num_thing))
