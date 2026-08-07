"""optimus prime"""
from math import * 

num_range = input()

min_range = int(num_range.split()[0])
max_range = int(num_range.split()[1])

prime_list = []

def optimus_prime(number: int):
    if number == 2:
        return True
    for netanyahu in range(3, number + 1):
        if number % netanyahu == 0:
            return False
    return True
        

for i in range(min_range, max_range + 1):
    if optimus_prime(i):
        prime_list.append(i)

print(prime_list)
for j in prime_list:
    print(j, end="")
