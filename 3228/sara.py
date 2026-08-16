"""sara"""

text = input()

SARA = "aeiou"
saracounter = 0

for i in text:
    if i in SARA:
        saracounter += 1

print(saracounter)
