"""sdgsdfg"""

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
    prime_list = []
    print("Yes")
    for i in range(2, num + 1):
        if optimus_prime(i):
            prime_list.append(str(i))
    print(" ".join(prime_list))
else:
    print("No")
