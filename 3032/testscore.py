"""testscore"""

bnuuy_num = int(input())

bnuuys = []

while bnuuy_num > 0:
    score = int(input())
    bnuuys.append(score)
    bnuuy_num -= 1

bnuuys.sort()
max_score = bnuuys[-1]

score_dupes = []

for i in bnuuys:
    if i != max_score:
        pass
    else:
        score_dupes.append(i)

print(max_score)
print(len(score_dupes))
