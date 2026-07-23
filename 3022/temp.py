"""temp calc"""

temp = float(input())
tempt = input()
finalt = input()

def convert(init_temp: float, temp_type: str, final_type: str):
    """converts temp from temp type to final type"""
    result = 0

    if (temp_type == final_type) and temp_type in ["K", "F", "C", "R"]:
        result = init_temp
    #celcius
    if temp_type == "C":
        if final_type == "K":
            result = init_temp + 273.15
        elif final_type == "R":
            result = (init_temp + 273.15) * (9 / 5)
        elif final_type == "F":
            result = init_temp * (9 / 5) + 32
    #fahrenhieht
    if temp_type == "F":
        if final_type == "C":
            result = (init_temp - 32) * (5 / 9)
        elif final_type == "R":
            result = init_temp + (273.15 * (9 / 5) - 32)
        elif final_type == "K":
            result = (init_temp - 32) * (5 / 9) + 273.15

    if temp_type == "R":
        if final_type == "K":
            result = init_temp * (5 / 9)
        elif final_type == "F":
            result = init_temp - (273.15 * (9 / 5) + 32)
        elif final_type == "C":
            result = (init_temp - (273.15 * (9 / 5))) * (5 / 9)

    if temp_type == "K":
        if final_type == "R":
            result = init_temp * (9 / 5)
        elif final_type == "C":
            result = init_temp + 273.15
        elif final_type == "F":
            result = (init_temp - 273.15) * (9 / 5) + 32

    return result

print(f"{convert(temp, tempt, finalt):.2f}")
