"""universal big lotto"""

ones = input().split()
tens = input().split()
hunds = input().split()

def compare(a, b, sym):
    """ffasfsf"""
    a, b = int(a), int(b)
    if sym == "==":
        return a == b
    if sym == "!=":
        return a != b
    if sym == ">":
        return a > b
    if sym == "<":
        return a < b
    if sym == ">=":
        return a >= b
    if sym == "<=":
        return a <= b
    return False

def domain(n, s2):
    """range"""
    result = []
    for j in range(10):
        if compare(j, n, s2):
            result.append(j)
    return result

for d in domain(hunds[1], hunds[0]):
    for i in range(d * 100, (d + 1) * 100):
        s = f"{i:03d}"
        if compare(s[1], tens[1], tens[0]) and compare(s[2], ones[1], ones[0]):
            print(s)
