"""power"""

expo = int(input())
pattern = [7, 9, 3, 1]

mod = expo % 4

print(pattern[mod - 1])
