"""agsdg"""
num = int(input())

if num == 1:
    print(1)
else:
    digits = 0
    start = 1
    length = 1

    while start <= num:
        end = min(start * 10 - 1, num)
        digits += (end - start + 1) * length
        start *= 10
        length += 1

    print(digits + num)
