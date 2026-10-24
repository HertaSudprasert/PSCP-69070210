"""stock"""

cmd_list = []

stocks = {}

while True:
    hi = input()
    command = hi.split()[0]

    if command == "END":
        break
    cmd_list.append(hi)

for cmds in cmd_list:
    raw = cmds.split()

    if len(raw) == 3:
        if raw[0] == "ADD":
            if raw[1] not in stocks:
                stocks.update({raw[1]: int(raw[2])})
            else:
                val = stocks[raw[1]]
                stocks.update({raw[1]: val + int(raw[2])})

        elif raw[0] == "REMOVE":
            val = stocks[raw[1]]
            if val < int(raw[2]):
                stocks[raw[1]] = 0
                print(f"Not enough stock for {raw[1]}")
            else:
                stocks[raw[1]] -= int(raw[2])

    else:
        if raw[0] == "CHECK":
            temp_list = []
            for k, v in stocks.items():
                if v < 5:
                    temp_list.append(k)

            if temp_list:
                temp_list.sort()
                for t in temp_list:
                    print(t)
            else:
                print("All stocks are sufficient")

        elif raw[0] == "REPORT":
            temp_list = []
            for k, v in stocks.items():
                temp_list.append(f"{k}: {v}")

            temp_list.sort()
            for t in temp_list:
                print(t)
