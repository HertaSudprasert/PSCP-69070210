"""n"""

big_list = input()

real_list = big_list.replace("[", "")
real_list = real_list.replace("]", "")
real_list = real_list.split(",")

for i in real_list:
    i = str(i)
    print(i[-1])
