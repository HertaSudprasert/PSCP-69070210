"""tua"""

data = input()

age = int(data.split()[0])
day = data.split()[1]

raka = 0

if age < 5:
    raka = 0
elif 5 <= age <= 18:
    raka = 100
else:
    raka = 150

if day == "Wed":
    raka /= 2

print(int(raka))
