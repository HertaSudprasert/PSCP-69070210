"""walk"""

direction = input()

pos = [0, 0]

walk = {
    "N": [0, 1],
    "S": [0, -1],
    "E": [1, 0],
    "W": [-1, 0]
}

for eachdir in direction:
    #adds walk vector to pos
    pos[0] += walk[eachdir][0]
    pos[1] += walk[eachdir][1]

d = abs(pos[0]) + abs(pos[1])

print(pos[0], pos[1], d)
