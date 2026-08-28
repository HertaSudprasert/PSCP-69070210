"""card"""

raw_card = input()

if len(raw_card) == 3:
    card_num = raw_card[0:2]
    card_type = raw_card[2]
else:
    card_num = raw_card[0]
    card_type = raw_card[1]

card1 = {
    "A": "ace",
    "J": "jack",
    "Q": "queen",
    "K": "king"
}

card2 = {
    "D": "diamonds",
    "H": "hearts",
    "S": "spades",
    "C": "clubs"
}

if not card_num.isdigit():
    print(f"{card1[card_num.upper()]} of {card2[card_type.upper()]}")
else:
    print(f"{card_num} of {card2[card_type.upper()]}")
