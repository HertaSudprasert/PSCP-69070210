"""113"""

raw = input()

def un113er(bruh: str):
    """remove 113"""
    return bruh.replace("113", "")

while True:
    if "113" in raw:
        raw = un113er(raw)
    else:
        break

print(raw)
