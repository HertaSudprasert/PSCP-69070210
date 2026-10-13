"""IJUDGE"""

link = input()

IJUDGE = "https://ijudge.it.kmitl.ac.th/problems/"
link_check = ""

n = 0
for asas in link:
    if n < 39:
        link_check += asas
    n += 1

def link_formatter(thing: str):
    """format string"""
    if link_check not in IJUDGE:
        print("INVALID")
        return

    thing = thing.replace(IJUDGE, "")
    thing = thing.replace("/", "")
    stuff = "-+=*/@#$%^()"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if len(thing) != 4:
        print("INVALID")
        return

    if not thing.isdigit():
        print("INVALID")
        return

    for j in thing:
        if j.lower() in alphabet:
            print("INVALID")
            return
        if j in stuff:
            print("INVALID")
            return

    for i in thing:
        if int(i) == 3:
            print("3 STAR")
            return
        if int(i) == 2:
            print("2 STAR")
            return
        if int(i) == 1:
            print("1 STAR")
            return
        if not int(i):
            print("0 STAR")
            return
        if int(i) not in (1, 2, 3, 4):
            print("INVALID")
            return

link_formatter(link)
