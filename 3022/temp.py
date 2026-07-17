"""temp calc"""

init_temp = float(input())
temp_type = input()
final_type = input()

def tocelcius(temp: float, temp_type: str):
    if temp_type == "K":
        return temp - 273.15
    elif temp_type == "F":
        return (temp - 32) * 5 / 9
    elif temp_type == "C":
        return temp
    elif temp_type == "R":
        return (temp * 5/9) -273.15

converted_to_c = tocelcius(init_temp, temp_type)

def tofinal(temp: float, final_type: str):
    if final_type == "C":
        return temp
    elif final_type == "K":
        return temp + 273.105
    elif final_type == "R":
        return (temp + 273.15) * 9 / 5
    elif final_type == "F":
        return temp * 9 / 5 + 32

print(f"{tofinal(converted_to_c, final_type):.2f}")
