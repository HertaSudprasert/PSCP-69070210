"""sddsdsd"""

data = input()
parcel = float(input())

start = data.split()[0]
dest = data.split()[1]

sen_thang = {
    "BKK": {
        "CNX": {
            "SP": 10,
            "PP": 30
        },
        "PKT": {
            "SP": 25,
            "PP": 50
        },
    },
    "CNX": {
        "UBP": {
            "SP": 15,
            "PP": 40
        },
    },
    "UBP": {
        "BKK": {
            "SP": 20,
            "PP": 40
        },
        "PKT": {
            "SP": 40,
            "PP": 70
        },
    },
    "PKT": {
        "CNX": {
            "SP": 30,
            "PP": 60
        },
    }
}

if dest not in sen_thang[start]:
    print("Error")
else:
    price = sen_thang[start][dest]["SP"] + (sen_thang[start][dest]["PP"] * parcel)

    print(f"{price:.2f}")
