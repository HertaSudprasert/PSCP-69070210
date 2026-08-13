"""pod"""

set1 = input()

#N people
N = int(set1.split()[0])
#K lines, pod capacity and the pod will มารับ when people of K แถวs appear
K = int(set1.split()[1])

line = []

for _ in range(0, N):
    thingamabob = int(input())
    line.append(thingamabob)

while all(people in line for people in range(1, K + 1)):
    for people in range(1, K + 1):
        line.remove(people)

print(len(line))
