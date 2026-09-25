"""faifa"""

import math

nuai = int(input())


def round_half_up(num, dec=0):
    mult = 10 ** dec
    return math.floor(num * mult + 0.5) / mult

kar_fai_base = 0

for i in range(1, nuai + 1):
    if 1 <= i <= 10:
        kar_fai_base += 5
    elif 11 <= i <= 50:
        kar_fai_base += 7
    elif 51 <= i <= 100:
        kar_fai_base += 10
    elif 101 <= i <= 200:
        kar_fai_base += 12
    else:
        kar_fai_base += 15

ft = nuai * 0.5

VAT = kar_fai_base * 0.07

print(f"{(kar_fai_base + ft + VAT):.1f}")
