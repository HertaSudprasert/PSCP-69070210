"""sss"""

raw = input()

cooked = raw.split()

cooked.reverse()

ffasf = []

for i in cooked:
    i = int(i)
    if not i % 3 or not i % 5:
        ffasf.append(i)

if not ffasf:
    print("Nope")
else:
    for j in ffasf:
        print(j)
