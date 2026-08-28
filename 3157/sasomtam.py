"""somtam"""

nigga = int(input())

instructions = []
netanyahu = 0

for _ in range(0, nigga):
    huhu = input()
    instructions.append(huhu)

for i in instructions:
    if i == "+":
        netanyahu += 10
    else:
        netanyahu -= 5

print(netanyahu)
