"""fence"""
luad = input()
price = int(input())

width = int(luad.split()[0])
length = int(luad.split()[1])
layers = int(luad.split()[2])

total_luad_length = 2 * (width + length) * layers
total_luad_price = total_luad_length * price

print(total_luad_length)
print(total_luad_price)
