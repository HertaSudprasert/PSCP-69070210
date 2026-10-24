"""gsdsd"""

raw = input()

seen = set()
left = ""

for i in raw:
    if i not in seen:
        seen.add(i)
        if raw.count(i) % 2:
            left += i

if not left:
    print("fully paired")
else:
    print(left)
