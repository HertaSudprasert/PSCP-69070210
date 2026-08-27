"""bonus"""

data = input()

panakngan = data.split()[0]
workage = int(data.split()[1])
salary = int(data.split()[2])

bonusthing = {
    "L5": {
        "M": 6,
        "B": 5,
        "G": 4
    },
    "5T10": {
        "M": 8,
        "B": 6,
        "G": 5
    },
    "M10": {
        "M": 10,
        "B": 7,
        "G": 6
    },
}

extra = {
    "M": 1500,
    "B": 1000,
    "G": 500
}
if workage <= 5:
    workage = "L5"
elif 5 < workage <= 10:
    workage = "5T10"
else:
    workage = "M10"

bonus = salary * (bonusthing[workage][panakngan] * 0.01)
bonus += extra[panakngan]

print(int(bonus))
