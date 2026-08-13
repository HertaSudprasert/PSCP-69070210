"""looping the rooms"""

room = int(input())

floor_num = 1

while room > (floor_num ** 2):
    floor_num += 1

destroy_wall = 0
if room % 2 == floor_num % 2:
    destroy_wall = 2 * (floor_num - 1)
else:
    destroy_wall = 2 * (floor_num - 1) - 1

print(destroy_wall)
