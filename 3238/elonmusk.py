"""absolute brute force elongaged muskrat programming"""

from math import floor

set1 = input()

num = int(set1.split()[0])
char = set1.split()[1]

alphabet = [
    "A", "B", "C", "D", "E", 
    "F", "G", "H", "I", "J", 
    "K", "L", "M", "N", "O", 
    "P", "Q", "R", "S", "T", 
    "U", "V", "W", "X", "Y", 
    "Z"
]

index = 0
index_start = 0

if char.isalpha():
    index = alphabet.index(char.upper())
    index_start = int(index + num / 2)

for line_num in range(0, num):
    each_line = "-" * num
    each_line_list = list(each_line)

    line_start = 1 + line_num
    line_end = num - line_num

    if not char.isalpha():
        each_line_list[line_start - 1] = char
        each_line_list[line_end - 1] = char
    else:
        if char.isupper():
            each_line_list[line_start - 1] = alphabet[index_start]
            each_line_list[line_end - 1] = alphabet[index_start]
        else:
            each_line_list[line_start - 1] = alphabet[index_start].lower()
            each_line_list[line_end - 1] = alphabet[index_start].lower()

        if  line_num < floor(num / 2):
            index_start -= 1
        else:
            index_start += 1
    print("".join(each_line_list))
