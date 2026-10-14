"""asfasf"""

band1 = input()
band2 = input()
band3 = input()
band4 = input()

bnum = {
    "Black": 0,
    "Brown": 1,
    "Red": 2,
    "Orange": 3,
    "Yellow": 4,
    "Green": 5,
    "Blue": 6,
    "Purple": 7,
    "Grey": 8,
    "White": 9

}

multiplier = {
    "Black": 1,
    "Brown": 10,
    "Red": 100,
    "Orange": 1000,
    "Yellow": 10000,
    "Green": 100000,
    "Blue": 1000000,
    "Purple": 10000000,
    "Gold": 0.1,
    "Silver": 0.01
}

tolerance = {
    "Brown": 1,
    "Red": 2,
    "Green": 0.5,
    "Blue": 0.25,
    "Purple": 0.10,
    "Grey": 0.05,
    "Gold": 5,
    "Silver": 10
}

def resistor(b1: str, b2: str, b3: str, b4: str):
    """do not resist"""
    if b1 not in bnum or b2 not in bnum\
        or b3 not in multiplier or b4 not in tolerance:
        print("Error")
        return

    resistance = int(str(bnum[b1]) + str(bnum[b2])) * multiplier[b3]
    lower = resistance * (1 - tolerance[b4] / 100)
    upper = resistance * (1 + tolerance[b4] / 100)

    print(f"{lower:.4f}")
    print(f"{upper:.4f}")

resistor(band1, band2, band3, band4)
