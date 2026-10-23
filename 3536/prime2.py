"""optimus prime"""

num = int(input())

def optimus_prime(number: int):
    """check if prime"""
    if number <= 1:
        return False

    for n in range(2, int(number ** 0.5) + 1):
        if not number % n:
            return False

    return True

if optimus_prime(num):
    print("YES")
else:
    print("NO")
