"""thai doesnt help"""

name = input()
age = int(input())
income = int(input())
status = input()
family = int(input())

def mega_thai_chuy_thai_considerer():
    """sg"""
    money = 0
    radab = ""
    if age < 18:
        print(f"{name} NOT ELIGIBLE")
        return

    if status == "Y":
        radab = "GOLD"
    else:
        if income <= 15000:
            radab = "GOLD"
        elif income <= 30000:
            radab = "SILVER"
        else:
            print(f"{name} NOT ELIGIBLE")
            return

    if radab == "GOLD":
        money += 3000
        if family >= 3:
            money += 500
    elif radab == "SILVER":
        money += 1500
        if family >= 3:
            money += 500

    print(name, radab, money)

mega_thai_chuy_thai_considerer()
