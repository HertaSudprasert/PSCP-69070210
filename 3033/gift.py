"""gift"""


nums = input()

radius = float(nums.split()[0])
height = float(nums.split()[1])
glue = float(nums.split()[2])

PI = 3.14

circle_circum = 2 * PI * radius

print(f"{(height + 2 * radius):.2f}" ,f"{(circle_circum + glue):.2f}")
