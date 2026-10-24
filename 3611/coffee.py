"""i neeed coffee"""

normal_coffee_price = float(input())
sale_b = float(input())
sale_c = float(input())
d_bath = float(input())
this_much_coffee = float(input())

promo1 = normal_coffee_price + (this_much_coffee - 1) * normal_coffee_price * (1 - sale_b / 100)
original_t = normal_coffee_price * this_much_coffee

if original_t >= d_bath:
    promo2 = original_t * (1 - sale_c / 100)
else:
    promo2 = original_t

if promo1 < promo2:
    print(1)
else:
    print(2)

print(f"{min(promo1, promo2):.2f}")
