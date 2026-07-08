"""buffet"""

promaxpay = int(input())
proactualpay = int(input())
priceperperson = int(input())
people = int(input())

paying = people - (people // promaxpay) * (promaxpay - proactualpay)

print(paying * priceperperson)
