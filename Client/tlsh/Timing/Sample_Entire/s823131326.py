def select(S):
    for i in range(0, n):
        minj = i
        for j in range(i, n):
            if int(S[j][1]) < int(S[minj][1]):
                minj = j
        (S[i], S[minj]) = (S[minj], S[i])
    return S

def bubble(B):
    flag = True
    while flag:
        flag = False
        for j in reversed(range(1, n)):
            if int(B[j][1]) < int(B[j-1][1]):
                (B[j-1], B[j]) = (B[j], B[j-1])
                flag = True
    return B

n = int(input())
A = input().split(' ')

B = bubble(A[:])
print(" ".join(B[:]))
print("Stable")
S = select(A)
print(" ".join(S))
print("Stable" if " ".join(B) == " ".join(S) else "Not stable")