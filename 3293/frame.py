"""big frame"""

thing = []

biggest = 0

for _ in range(0, 5):
    a = input().strip()
    thing.append(a)
    if len(a) > biggest:
        biggest = len(a)

print("*" * (biggest + 4))
for j in thing:
    padding = biggest - len(j)
    print("* " + j + (" " * padding) + " *")
print("*" * (biggest + 4))
