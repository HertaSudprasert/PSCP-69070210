"""huy"""

actual_huy = input()
huy = input()

ah_letter = actual_huy[0]
ah_num = actual_huy[2:6]

h_letter = huy[0]
h_num = huy[2:6]

def huy_processor():
    """processes huy"""

    value = 0

    if h_letter == ah_letter:
        if h_num == ah_num:
            value = 1000000
        elif h_num[2:] == ah_num[2:]:
            value = 2000
        elif h_num[3:] == ah_num[3:]:
            value = 1000
        elif h_num != ah_num:
            value = 20
    elif h_letter != ah_letter:
        if h_num == ah_num:
            value = 100000
        elif h_num[2:] == ah_num[2:]:
            value = 200
        elif h_num[3:] == ah_num[3:]:
            value = 100
        elif h_num != ah_num:
            value = 0
    else:
        value = 0

    return value

print(huy_processor())
