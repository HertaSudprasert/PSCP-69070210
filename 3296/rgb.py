"""rgb"""

color1 = input().split()
color2 = input().split()

avg1 = (int(color1[0]) + int(color2[0])) // 2
avg2 = (int(color1[1]) + int(color2[1])) // 2
avg3 = (int(color1[2]) + int(color2[2])) // 2

print(avg1, avg2, avg3)
