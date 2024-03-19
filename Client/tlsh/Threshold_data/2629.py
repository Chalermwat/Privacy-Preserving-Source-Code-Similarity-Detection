def main():
    N = int(input())
    A = []
    temp = 0
    sum = 0
    i = 1
    while True:
        temp = 0
        i += 1
        sum += 1
        for j in range(1,i,1):
            temp += 26**j
        if N <= temp:
            break
    #print(sum)
    if sum == 1:
        N = N-1
    else:
        temp = 0
        for j in range(1,sum):
            temp += 26**j
        N -= (temp+1)

    for j in range(sum):
        #print(N)
        amari = N % 26
        N = N // 26
        A.append(amari)
        #print(A)
    #print(A)

    B = [0]*len(A)
    for i in range(len(A)-1,-1,-1):
        dict = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
        B[i] = dict[A[i]]

    ans = [0]*len(B)
    for j in range(len(B)):
        ans[j] = B[len(B)-1-j]

    print(''.join(ans))

main()
