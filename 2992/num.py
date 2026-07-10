"""num"""

num = input()
symbol = input()

normal_num = int(num)
reversed_num = int(num[::-1])

if symbol == "+":
    result = normal_num + reversed_num
    print(f"{normal_num} + {reversed_num} = {result}")
elif symbol == "*":
    result = normal_num * reversed_num
    print(f"{normal_num} * {reversed_num} = {result}")
