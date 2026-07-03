"""dshshsh"""

name = input()
surname = input()
age = input()

if len(name) >= 5 and len(surname) >= 5:
    passwd = name[:2] + surname[-1] + age[-1]
    print(passwd)
else:
    passwd = name[0] + age + surname[-1]
    print(passwd)
