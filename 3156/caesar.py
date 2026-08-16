"""caesar"""

text = input()
offset = int(input())

offset = offset % 26

alphabet = [
    "A", "B", "C", "D", "E", 
    "F", "G", "H", "I", "J", 
    "K", "L", "M", "N", "O", 
    "P", "Q", "R", "S", "T", 
    "U", "V", "W", "X", "Y", 
    "Z"
]

for i in text:
    index = alphabet.index(i.upper())
    new_index = index + offset
    if new_index >= 26:
        new_index = new_index % 26

    print((alphabet[new_index]).lower(), end="")
