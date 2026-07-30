"""brick"""

smolbrick = int(input())
bigbrick = int(input())
goal = int(input())

def bridgebuilder():
    """builds bridge"""
    chai_it_lek = None
    chai_it_yai = goal // 5
    
    if bigbrick * 5 > goal:
        chai_it_lek = goal - ((chai_it_yai) * 5)
        if smolbrick < chai_it_lek:
            chai_it_lek = -1

    elif bigbrick * 5 == goal:
        chai_it_lek = 0

    elif bigbrick * 5 < goal:
        chai_it_lek = goal - (bigbrick * 5)
        if smolbrick < chai_it_lek:
            chai_it_lek = -1

    return chai_it_lek

print(bridgebuilder())
