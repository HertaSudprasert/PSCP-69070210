"""color"""

col1 = input()
col2 = input()

if col1 == "Red" and col2 == "Yellow":
    print("Orange")
elif col2 == "Red" and col1 == "Yellow":
    print("Orange")
elif col1 == "Red" and col2 == "Blue":
    print("Violet")
elif col2 == "Red" and col1 == "Blue":
    print("Violet")
elif col1 == "Yellow" and col2 == "Blue":
    print("Green")
elif col2 == "Yellow" and col1 == "Blue":
    print("Green")
elif (col1 == col2) and col1 in ["Red", "Yellow", "Blue"]:
    print(col1)
else:
    print("Error")
