"""historgram"""

text = input()
letters = [c for c in text if c.isalpha()]
unique = sorted(list(set(letters)), key=lambda x: (x.lower(), x.isupper()))

for c in unique:
    count = letters.count(c)
    print(f"{c} = {count}")
