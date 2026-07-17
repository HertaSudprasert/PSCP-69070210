"""harn long tua"""

N = int(input())

harn_long_tua_list = []

for i in range(0, N + 1):
    if not i % 10:
        harn_long_tua_list.append(i)

harn_long_tua_list.sort(reverse=True)
harn_long_tua_string = ""

for i in harn_long_tua_list:
    harn_long_tua_string += str(i)
    harn_long_tua_string += " "

print(harn_long_tua_string)
