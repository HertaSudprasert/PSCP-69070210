"""sdsdsdg"""
num = int(input())

def is_square_free(n: int):
    """check if sq free"""
    i = 2
    while i * i <= n:
        if not n % (i * i):
            return False

        i += 1
    return True

sq = 0

for eee in range(1, num + 1):
    if is_square_free(eee):
        sq += 1

print(sq)
