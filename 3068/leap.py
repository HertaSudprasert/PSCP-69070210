"""leapyear"""
y = int(input())

def is_leap_year(year: int):
    """check if leap year"""

    if year <= 1582:
        if not year % 4:
            print("yes")
        else:
            print("no")
        return

    if not year % 4:
        if not year % 100:
            if not year % 400:
                print("yes")
                return
            print("no")
            return
        print("yes")
    else:
        print("no")

is_leap_year(y)
