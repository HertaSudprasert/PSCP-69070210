"""airport"""

timein = input()
timeout = input()

timein_hr = int(timein.split(".")[0])
timein_min = int(timein.split(".")[1] )

timeout_hr = int(timeout.split(".")[0])
timeout_min = int(timeout.split(".")[1])

timein = (timein_hr * 60) + timein_min
timeout = (timeout_hr * 60) + timeout_min

parking_time = timeout - timein

if parking_time % 60:
    if parking_time % 60 <= 15 and parking_time < 60:
        parking_time = 0
    else:
        parking_time -= parking_time % 60
        parking_time += 60

parking_time //= 60

kar_jord_rod = {
    0: "FREE",
    1: 25,
    2: 50,
    3: 80,
    4: 110,
    5: 145,
    6: 180,
    7: 250
}

if parking_time > 24 or parking_time < 0:
    print("ERROR")
elif parking_time > 7:
    print(250)
else:
    print(kar_jord_rod[parking_time])
