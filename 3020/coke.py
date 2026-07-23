"""coke"""
#a >= 0
old_price = int(input())
#b >= 0
fakuad = int(input())
#a >= c >= 0
extra_bottle_price = int(input())
#d >= 0
want_this_much_bottle = int(input())



if fakuad:
    KUAD_SALE_NUM = (want_this_much_bottle - 1) // fakuad
else:
    KUAD_SALE_NUM = 0

normal_kuad_num = want_this_much_bottle - KUAD_SALE_NUM

price = (normal_kuad_num * old_price) + (KUAD_SALE_NUM * extra_bottle_price)

if not want_this_much_bottle:
    price = 0

print(price)
