"""bill"""

price = int(input())

borigarn_price = price * 0.1

if borigarn_price < 50:
    borigarn_price = 50
elif borigarn_price > 1000:
    borigarn_price = 1000

pasee = (price + borigarn_price) * 0.07

final_price = price + borigarn_price + pasee

print(f"{final_price:.2f}")
