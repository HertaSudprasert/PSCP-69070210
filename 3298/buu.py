"""labuubuu"""

thing = input()

MAX_U = 0

def check_thing(substr: str):
    """ddddd"""
    global MAX_U
    ct = 0
    for char in substr:
        if char.upper() == "U":
            ct += 1
            if ct > MAX_U:
                MAX_U = ct
        else:
            ct = 0
            return

if "BUU" in thing.upper():
    for i, j in enumerate(thing):
        if j.upper() == "B":
            check_thing(thing[i + 1:])
    print("Yes", MAX_U)
elif "B" in thing.upper():
    index = thing.upper().find("B")
    print(thing[:index] + ("U" * (len(thing) - (index + 1))))
else:
    buu = ["B", "U", "U"]
    for i in range(0, len(thing)):
        print(buu[i % 3], end="")
    print()
