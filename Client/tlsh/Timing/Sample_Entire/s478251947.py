def BubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A)-1,i,-1):  
            
            if A[j][1] < A[j-1][1]:
                # リストの要素の文字列は2次元配列として記憶される
                A[j],A[j-1] = A[j-1],A[j]
    return A

def SelectionSort(A):
    for i in range(len(A)):
        mini = i
        for j in range(i,len(A)):
            if A[j][1] < A[mini][1]:
                mini = j
        A[i],A[mini] = A[mini],A[i]
    return A


N = int(input())
# example for input to array : H4 C9 S4 D2 C3 (from cards)
array = [i for i in input().split()]
array_cp = list(array)

result_bs = BubbleSort(array)
print(*result_bs)
print('Stable') # Bubble sort is stable

result_ss = SelectionSort(array_cp)
print(*result_ss)
if result_ss == result_bs:
    print('Stable')
else:
    print('Not stable')
