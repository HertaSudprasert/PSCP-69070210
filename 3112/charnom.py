"""charnom"""

import math

kaimook_data = input()
charnom_data = input()

kaimook_type = kaimook_data.split()[0]
kaimook_num = float(kaimook_data.split()[1])

char_type = charnom_data.split()[0]
char_sweet = charnom_data.split()[1]
char_amount = float(charnom_data.split()[2])

char_dict = {
    "R": {
        "1": 12,
        "2": 18,
        "3": 25
    },
    "T": {
        "1": 15,
        "2": 20,
        "3": 30
    },
    "M": {
        "1": 10,
        "2": 15,
        "3": 20
    }
}

kaimook_dict = {
    "H": 5,
    "O": 3,
    "J": 2,
}

def char_analyzer():
    """analyzes char"""
    kaimook = kaimook_dict[kaimook_type] * kaimook_num
    char = char_dict[char_type][char_sweet] * char_amount
    palang_ngan_char =  kaimook + char

    if palang_ngan_char.is_integer():
        print(math.floor(palang_ngan_char))
    else:
        print(palang_ngan_char)
        
char_analyzer()
