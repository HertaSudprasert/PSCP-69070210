"""temp calc"""

temp = float(input())
tempt = input()
finalt = input()

def toc(init_temp: float, temp_type: str):

    """any temp to celcius"""

    result = 0
    if temp_type == "K":
        result = init_temp - 273.15
    elif temp_type == "F":
        result = (init_temp - 32) * 5 / 9
    elif temp_type == "C":
        result = init_temp
    elif temp_type == "R":
        result = init_temp * 5 / 9 - 273.15

    return result

c_temp = toc(temp, tempt)

result2 = 0

if finalt == "C":
    result2 = c_temp
elif finalt == "K":
    result2 = c_temp + 273.15
elif finalt == "F":
    result2 = c_temp * 9 / 5 + 32
elif finalt == "R":
    result2 = (c_temp + 273.15) * 9 / 5

print(f"{result2:.2f}")
