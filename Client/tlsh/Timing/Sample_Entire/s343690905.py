def bubble_sort(card_list):
    cards = [i for i in card_list]
    list_length = len(cards)

    for i in range(list_length):
        for j in range(list_length-1,i,-1):
            if int(cards[j][1:]) < int(cards[j-1][1:]):
                cards[j],cards[j-1] = cards[j-1],cards[j]
    return cards

def selection_sort(card_list):
    cards = [i for i in card_list]

    list_length = len(cards)

    for i in range(list_length):
        min_element = i
        for j in range(i+1,list_length):
            if int(cards[j][1:]) < int(cards[min_element][1:]):
                min_element = j
        cards[i],cards[min_element] = cards[min_element],cards[i]
    return cards

n = int(input())
cards = input().split()
bubble_cards = bubble_sort(cards)
selection_cards = selection_sort(cards)

print(' '.join(bubble_cards))
print('Stable')
print(' '.join(selection_cards))
if bubble_cards == selection_cards:
    print('Stable')
else:
    print('Not stable')
