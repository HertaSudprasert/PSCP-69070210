"""labuubuu"""

thing = input()

if "BUU" in thing.upper():
    counter = 0
    max_u = 0
    for i, j in enumerate(thing):
        print(i, j)
        if j.upper() == "B":
            for char in thing[i:]:
                
                if char.upper() == "U":
                    counter += 1
                    if counter > max_u:
                        max_u = counter
                else:
                    counter = 0

            

print(max_u)