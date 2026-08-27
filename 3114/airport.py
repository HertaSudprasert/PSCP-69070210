"""airport"""

timein = input()
timeout = input()

timein_parts = timein.split(".")
timeout_parts = timeout.split(".")

if len(timein_parts) != 2 or len(timeout_parts) != 2:
    print("ERROR")

elif not all(x.isdigit() for x in timein_parts + timeout_parts):
    print("ERROR")

else:
    timein_hr = int(timein_parts[0])
    timein_min = int(timein_parts[1])
    timeout_hr = int(timeout_parts[0])
    timeout_min = int(timeout_parts[1])

    if not (
        0 <= timein_hr <= 23
        and 0 <= timein_min <= 59
        and 0 <= timeout_hr <= 23
        and 0 <= timeout_min <= 59
    ):
        print("ERROR")

    else:
        timein = timein_hr * 60 + timein_min
        timeout = timeout_hr * 60 + timeout_min

        parking_time = timeout - timein

        if parking_time < 0:
            print("ERROR")

        elif parking_time <= 15:
            print("FREE")

        else:
            parking_hours = (parking_time + 59) // 60

            kar_jord_rod = {
                1: 25,
                2: 50,
                3: 80,
                4: 110,
                5: 145,
                6: 180
            }

            if parking_hours > 24:
                print("ERROR")
            elif parking_hours >= 7:
                print(250)
            else:
                print(kar_jord_rod[parking_hours])
