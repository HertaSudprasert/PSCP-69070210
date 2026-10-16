"""dsgsd"""

menu = []
while True:
    line = input()
    if line == "DONE":
        break
    if line == "CLOSED":
        menu.clear()
        break
    if line == "SOMETHING'S WRONG":
        menu.clear()
    elif line.startswith("Can't do: "):
        dish = line[len("Can't do: "):]
        if dish in menu:
            menu.remove(dish)
    else:
        if " #" in line:
            dish, pos_str = line.rsplit(" #", 1)
            if pos_str == "N":
                menu.append(dish)
            else:
                pos = int(pos_str)
                menu.insert(pos - 1, dish)

reversed_menu = menu[::-1]

print(f"Full Course: {menu} Reversed: {reversed_menu}")
