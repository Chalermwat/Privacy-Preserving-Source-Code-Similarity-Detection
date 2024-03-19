N = int(input())
A = list(input().split())
A_copy = A[:]

def bubble_sort(N, A):
  flag = 1
  sorted_index = 0
  while flag:
    flag = 0
    for i in range(N-1, sorted_index, -1):  # N-1からソート済みのインデックス番号まで降順
      if A[i][1] < A[i-1][1]:
        temp = A[i]
        A[i] = A[i-1]
        A[i-1] = temp
        flag = 1
    sorted_index += 1

def selection_sort(N, A):
  for i in range(0, N-1):
    minj = i
    for j in range(i+1, N):
      if A[j][1] < A[minj][1]:
        minj = j
    if i is not minj:
      temp = A[i]
      A[i] = A[minj]
      A[minj] = temp

bubble_sort(N, A)
selection_sort(N,A_copy)
print(' '.join(map(str, A)))
print('Stable')
print(' '.join(map(str, A_copy)))
if A == A_copy:
  print('Stable')
else:
  print('Not stable')

