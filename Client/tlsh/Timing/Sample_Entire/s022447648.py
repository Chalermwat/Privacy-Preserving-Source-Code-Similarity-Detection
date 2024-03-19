# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 10:01:05 2017

@author: syaga
"""

if __name__ == "__main__":
    N = int(input())
    C = list(input().split())
    D = C[:]

    # Bunbble Sort
    for i in range(0, N):
        for j in range(N-1, i, -1):
            if int(C[j][1]) < int(C[j-1][1]):
                temp = C[j]
                C[j] = C[j-1]
                C[j-1] = temp
    print(" ".join(C))
    print("Stable")

    # Selection Sort
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if int(D[j][1]) < int(D[minj][1]):
                minj = j
        temp = D[i]
        D[i] = D[minj]
        D[minj] = temp
    print(" ".join(D))
    flag = 0
    for (i, j) in zip(C, D):
        if i != j:
            flag = 1
            break
    if flag == 1:
        print("Not stable")
    else:
        print("Stable")