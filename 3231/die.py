"""fgdfshdf"""

guess = int(input())
die = int(input())

def mega_thing():
    """fgdffh"""
    if 1 > guess or guess > 6:
        print("Invalid")
        return
    if 1 > die or die > 6:
        print("Invalid")
        return

    if guess == die:
        print("Correct!")
    else:
        print("Wrong!")

mega_thing()
