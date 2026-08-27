"""promotion"""

data = input()

dinsor = int(data.split()[0])
samud = int(data.split()[1])
glong_see = int(data.split()[2])

list_of_things = [dinsor, samud, glong_see]

raka = (dinsor * 25) + (samud * 40) + (glong_see * 55)

if sum(list_of_things) >= 3:
    raka = raka - (raka * 0.1)

print(int(raka))
