import collections

Card = collections.namedtuple('Card', ['suit', 'value'])


def bubble_sort(array):
    a = array[::]
    for i in range(len(a)):
        for j in reversed(range(i + 1, len(a))):
            if a[j].value < a[j - 1].value:
                a[j], a[j - 1] = a[j - 1], a[j]
    return a


def selection_sort(array):
    a = array[::]
    for i in range(len(a)):
        min_j = i
        for j in range(i, len(a)):
            if a[j].value < a[min_j].value:
                min_j = j
        a[i], a[min_j] = a[min_j], a[i]
    return a


if __name__ == '__main__':
    n = int(input())
    cards = [Card(suit, int(value)) for suit, value in input().split()]
    stable = sorted(cards, key=lambda a: a.value)

    bubble = bubble_sort(cards)
    print(' '.join(''.join(map(str, card)) for card in bubble))
    print('Stable' if bubble == stable else 'Not stable')

    selection = selection_sort(cards)
    print(' '.join(''.join(map(str, card)) for card in selection))
    print('Stable' if selection == stable else 'Not stable')