"""safasf"""

num = int(input())

nom = []
normal_num = list(range(1, num + 1))

while True:
    temp = int(input())
    if not temp:
        break
    nom.append(temp)

nom.sort()

diff = set(nom) ^ set(normal_num)
for i in diff:
    print(i)
