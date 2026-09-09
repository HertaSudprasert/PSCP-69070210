"""13"""

thing = input()

if int(thing[0]) > 5:
    FIRST_DIG = 9
elif int(thing[1]) > 5:
    FIRST_DIG = 10
elif int(thing[2]) > 5:
    FIRST_DIG = 11
elif int(thing[3]) > 5:
    FIRST_DIG = 12
elif int(thing[4]) > 5:
    FIRST_DIG = 14
else:
    FIRST_DIG = 13

def is_palindrome(num: str):
    """find palindrome"""
    if (num[0] == num[4]) and (num[1] == num[3]):
        return True
    return False

if is_palindrome(thing):

    if int(thing[0]) + int(thing[4]) > 5:
        SECOND_DIG = 1
    elif int(thing[1]) * int(thing[3]) > 5:
        SECOND_DIG = 2
    else:
        SECOND_DIG = 0
else:
    if int(thing[4]) and int(thing[0]) // int(thing[4]) > 5:
        SECOND_DIG = 1
    elif int(thing[1]) - int(thing[4]) > 5:
        SECOND_DIG = 2
    else:
        SECOND_DIG = 0

sum_thing = 0
prod_thing = 1
for i in thing:
    sum_thing += int(i)
    prod_thing *= int(i)

if sum_thing > 25:
    THIRD_DIG = 1
elif prod_thing > 55:
    THIRD_DIG = 2
else:
    THIRD_DIG = 0

print(f"{FIRST_DIG}{SECOND_DIG}{THIRD_DIG}")
