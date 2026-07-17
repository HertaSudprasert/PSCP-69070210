"""coke"""
#a >= 0
old_price = int(input)
#b >= 0
fakuad = int(input)
#a >= c >= 0
new_price = int(input)
#d >= 0
want_this_much_bottle = int(input)
if fakuad != 0:
    fakuad_per_bath = ( old_price - new_price ) / fakuad
    result = want_this_much_bottle * new_price
else:
    pass


