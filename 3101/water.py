"""water"""

temp = int(input())
temp_type = input()

if temp_type.lower() == "f":
    if temp <= 32:
        print("solid")
    elif 32 < temp < 212:
        print("liquid")
    else:
        print("gas")
elif temp_type.lower() == "c":
    if temp <= 0:
        print("solid")
    elif 0 < temp < 100:
        print("liquid")
    else:
        print("gas")
