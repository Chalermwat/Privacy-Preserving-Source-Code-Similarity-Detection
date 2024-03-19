N = int(input())
a = [(s[0], int(s[1])) for s in input().split()]

def bubble(a):
    n = len(a)
    for i in range(n):
        for j in range(n-1, i, -1):
            if a[j][1] < a[j-1][1]:
                a[j], a[j-1] = a[j-1], a[j]
    return a

def selection(a):
    n = len(a)
    for i in range(n):
        minj = i
        for j in range(i+1, n):
            if a[j][1] < a[minj][1]:
                minj = j
        a[i], a[minj] = a[minj], a[i]

    return a

b_a = bubble(a[:])
s_a = selection(a[:])

print(" ".join([p[0]+str(p[1]) for p in b_a]))
print("Stable")
print(" ".join([p[0]+str(p[1]) for p in s_a]))
print("Stable" if b_a==s_a else "Not stable")