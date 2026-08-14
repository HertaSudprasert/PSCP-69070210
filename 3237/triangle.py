"""triangle"""

num = int(input())

for line_num in range(0, num):
    line = ""
    for each_char in range(0, line_num + 1):

        if not each_char or (each_char == line_num):
            line += "0"
        else:
            line += "1"

        if line_num + 1 == num:
            line = "0" * num
    print(line)
