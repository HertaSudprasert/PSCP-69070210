"""f"""
import json

raw = input()
threshold = float(input())

cooked = json.loads(raw)

finished = {}

for k, v in cooked.items():
    if v >= threshold:
        finished.update({k: f"{v:.2f}"})

finished = dict(sorted(finished.items()))

if finished:
    for k, v in finished.items():
        print(k + "\t" + str(v))
else:
    print("Nope")
