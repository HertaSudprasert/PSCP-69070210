"""agdsg"""

nigga = int(input())

thing = []

for _ in range(0, nigga):
    doohickey = int(input())
    thing.append(doohickey)

yord_kai_sum = sum(thing)
thing.sort()

yord_kai_high = thing[-1]
yord_kai_low = thing[0]
yord_kai_avg = yord_kai_sum / len(thing)

print(yord_kai_sum)
print(yord_kai_high)
print(yord_kai_low)
print(f"{yord_kai_avg:.1f}")
