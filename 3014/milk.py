"""mommy milkers"""

price_per_bottol = int(input())
fakuad = int(input())
promotion = int(input())
money = int(input())

original_kuad_num = money // price_per_bottol
extra_milk = 0

if original_kuad_num >= fakuad > 0:
    extra_milk = ((original_kuad_num - fakuad) // (fakuad - promotion) + 1) * promotion

print(original_kuad_num + extra_milk)
