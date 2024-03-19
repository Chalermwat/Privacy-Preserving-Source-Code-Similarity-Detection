def comp(a,b):
    if a[1] > b[1]:
        return True
    else:
        return False

def bubble_sort(a):
    for i in range(n):
        for j in reversed(range(i+1,n)):
            if comp(a[j-1],a[j]):
                a[j],a[j-1]=a[j-1],a[j]
    return a

def selection_sort(a):
    for i in range(n):
        mini = i
        for j in range(i,n):
            if comp(a[mini],a[j]):
                mini=j
        a[mini],a[i]=a[i],a[mini]
    return a

def stable(original_a,sorted_a):
    for num in range(1,10):
        suite_ord = []
        for v in original_a:
            if v[1] == str(num):
                suite_ord.append(v[0])
        for v in sorted_a:
            if v[1] == str(num):
                if v[0]==suite_ord[0]:
                    del suite_ord[0]
                else:
                    return "Not stable"
    return "Stable"


n = int(raw_input())
cards = raw_input().split(' ')

sorted_cards = bubble_sort(cards[:])
print ' '.join(sorted_cards)
print stable(cards,sorted_cards)
sorted_cards = selection_sort(cards[:])
print ' '.join(sorted_cards)
print stable(cards,sorted_cards)