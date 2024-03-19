# coding: utf-8
# Here your code !
n=int(input())
cards=input().split()

def bubble_sort(cards_b,n):
    for i in range(n):
        for j in range(-1,-n,-1):
            a=int(cards_b[j][1])
            b=int(cards_b[j-1][1])
            if a<b:
                cards_b[j],cards_b[j-1]=cards_b[j-1],cards_b[j]
    return cards_b

def selection_sort(cards_s,n):
    for i in range(n):
        minv=i
        for j in range(i,n):
            a=int(cards_s[minv][1])
            b=int(cards_s[j][1])
            if a>b:
                minv=j
        cards_s[minv],cards_s[i]=cards_s[i],cards_s[minv]
    return cards_s


dummy=cards.copy()
ans_1=bubble_sort(cards,n)

ans_2=selection_sort(dummy,n)

print(*ans_1)
print("Stable")
print(*ans_2)
if ans_1!=ans_2:
    print("Not stable")
else:
    print("Stable")