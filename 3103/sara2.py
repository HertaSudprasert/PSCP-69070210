"""sara"""

num = int(input())

chars = []

while num > 0:
    char = input()
    chars.append(char)
    num -= 1

sara_counter = 0

for tua_ak_sorn in chars:
    if tua_ak_sorn in ["A", "E", "I", "O", "U"]:
        sara_counter += 1

print(sara_counter)
