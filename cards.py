card_deck=[4,11,8,5,13,2,10]
hand=[]
for card in card_deck:
    if sum(hand)<17:
        hand.append(card_deck.pop())
print(hand)  # [10, 2, 13]

while sum(hand)<17:
    hand.append(card_deck.pop())
print(hand)  # [10, 2, 13]

