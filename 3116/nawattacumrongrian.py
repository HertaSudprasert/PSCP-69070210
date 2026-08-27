"""nigga wtf is this incomprehensible problem"""

school = input()

thing = []
first = ord(school[0].upper())
last = ord(school[-1].upper())

for i in range(1, 11):
    val = i - 1

    if i % 2:
        rahas1 = first + val
    else:
        rahas1 = last - val
    rahas2 = rahas1 % len(school)

    if rahas2 > 9:
        rahas2 %= 10

    thing.append(rahas2)

mid = thing[2:8]

print(" ".join(map(str, mid)))
