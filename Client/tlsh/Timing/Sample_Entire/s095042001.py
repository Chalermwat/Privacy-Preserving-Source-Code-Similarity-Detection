# coding: utf-8

def bubble_sort(A, N):
    C = list(A)
    for i in xrange(N):
        for j in reversed(xrange(i+1, N)):
            if C[j][1] < C[j-1][1]:
                C[j], C[j-1] = C[j-1], C[j]
    return C

def selection_sort(A, N):
    C = list(A)
    for i in xrange(N):
        minj = i
        for j in xrange(i, N):
            if C[j][1] < C[minj][1]:
                minj = j
        C[i], C[minj] = C[minj], C[i]
    return C

def is_stable(a, c, n):
    for i in xrange(n-1):
        if c[i][1] == c[i+1][1]:
            if a.index(c[i]) > a.index(c[i+1]):
                print "Not stable"
                return False
    print "Stable"
    return True

def print_c(c):
    print " ".join(map(lambda c:c[0] + str(c[1]), c))

def main():
    n = input()
    c = map(lambda c:(c[0], int(c[1:])), raw_input().split())
    bubble = bubble_sort(c, n)
    selection = selection_sort(c, n)
    print_c(bubble)
    is_stable(c, bubble, n)
    print_c(selection)
    is_stable(c, selection, n)

main()