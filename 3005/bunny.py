"""bunny"""

groceries = input()

carrot = int(groceries.split()[0])
galampre = int(groceries.split()[1])
tomato = int(groceries.split()[2])

result = carrot * 10 + galampre * 25 + tomato * 3

print(result)
