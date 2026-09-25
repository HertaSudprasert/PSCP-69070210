"""labuubuu"""
thing = input()

MAX_U = 0

def check_thing(substr: str):
    """dddd"""
    ct = 0
    for char in substr:
        if char.upper() == "U":
            ct += 1
        else:
            return ct
    return ct

if "BUU" in thing.upper():
    for i, j in enumerate(thing):
        if j.upper() == "B":
            count = check_thing(thing[i + 1:])
            if count > MAX_U:
                MAX_U = count

    print("Yes", MAX_U)

elif "B" in thing.upper():
    index = thing.upper().find("B")
    print(thing[:index + 1] + ("U" * (len(thing) - (index + 1))))

else:
    buu = ["B", "U", "U"]
    for i in range(len(thing)):
        print(buu[i % 3], end="")
    print()
