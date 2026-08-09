"""optimus prime"""

num_range = input()

min_range = int(num_range.split()[0])
max_range = int(num_range.split()[1])

prime_list = []

def optimus_prime(number: int):
    """check if prime"""
    if number <= 1:
        return False

    for netanyahu in range(2, number):
        if not number % netanyahu:
            return False

    return True

for i in range(min_range, max_range + 1):
    if optimus_prime(i):
        prime_list.append(i)

if prime_list:
    print(" ".join(str(prim) for prim in prime_list))
print(f"Total primes: {len(prime_list)}")
