def bubble_sort(data):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1, i, -1):
            if int(data[j][1]) < int(data[j - 1][1]):
                data[j], data[j - 1] = data[j - 1], data[j]

def selection_sort(data):
    for i in range(len(data)):
        min_j = i
        for j in range(i, len(data)):
            if int(data[j][1]) < int(data[min_j][1]):
                min_j = j
        if min_j != i:
            data[i], data[min_j] = data[min_j], data[i]

input()
cards = [x for x in input().split()]
cards_b = cards.copy()
cards_s = cards.copy()
bubble_sort(cards_b)
selection_sort(cards_s)
for data in [cards_b, cards_s]:
    print(' '.join(data))
    if data == cards_b:
        print("Stable")
    else:
        print("Not stable")