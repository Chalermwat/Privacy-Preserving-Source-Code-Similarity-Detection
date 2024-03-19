def bubble_sort(C, N):
    card = []
    for c in C:
        card.append({'suit': c[0], 'value': int(c[1])})
            
    for i in range(N):
        for j in range(N-1, i, -1):
            if card[j]['value'] < card[j-1]['value']:
                card[j], card[j-1] = card[j-1], card[j]

    new_C = []
    for i in range(N):
        new_C.append(card[i]['suit'] + str(card[i]['value']))
        
    return new_C


def selection_sort(C, N):
    card = []
    for c in C:
        card.append({'suit': c[0], 'value': int(c[1])})

    for i in range(N):
        min_j = i
        for j in range(i, N):
            if card[j]['value'] < card[min_j]['value']:
                min_j = j
        card[i], card[min_j] = card[min_j], card[i]
        
    new_C = []
    for i in range(N):
        new_C.append(card[i]['suit'] + str(card[i]['value']))
        
    return new_C


N = int(input().rstrip())
C = input().rstrip().split()

C_b = bubble_sort(C, N)
C_s = selection_sort(C, N)

print(' '.join(C_b))
print('Stable')

print(' '.join(C_s))
if C_s == C_b:
    print('Stable')
else:
    print('Not stable')
