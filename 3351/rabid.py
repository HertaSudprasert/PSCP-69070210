"""rabid"""

raw = input().upper()
count = [0]

def check(txt, index, f, b):
    """check thing"""
    if f not in "RABIT":
        return False, index-1
    if b not in "RABIT":
        return False, index
    if index == 1 and f not in "ITRB":
        return False, index-1
    if f == "B" and b not in "IT":
        return False, index
    if f == "R" and b != "A":
        return False, index
    if f not in "RA" and b == "A":
        return False, index
    if index + 1 == len(txt) and b not in "AIT":
        return False, index
    return True, -1

output = "yes"

i = 1
while i < len(raw):
    prev = raw[i - 1]
    curr = raw[i]

    if prev == "A":
        count[-1] += 1
    if curr != "A":
        count.append(0)
    elif i + 1 == len(raw):
        count[-1] += 1
    is_valid, wrong_index = check(raw, i, prev, curr)
    if not is_valid:
        output = f"no {wrong_index}"
        break
    i += 1
    if "A" not in raw and "R" not in raw and "B" not in raw:
        output = f"unknown {len(raw)}"
    elif i == len(raw):
        output = f"yes {max(count)}"
print(output)
