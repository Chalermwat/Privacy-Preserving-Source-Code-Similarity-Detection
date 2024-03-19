def selectionSort(A, N):
	for i in range(N):
		minj = i
		for j in range(i, N):
			if A[j][1:] < A[minj][1:]:
				minj = j
		if i != minj:
			tmp = A[i]
			A[i] = A[minj]
			A[minj] = tmp

	return A

def bubbleSort(A, N):
	for i in range(N):
		for j in range(N - 1, i, -1):
			if A[j][1:] < A[j - 1][1:]:
				tmp = A[j]
				A[j] = A[j - 1]
				A[j - 1] = tmp

	return A

if __name__ == '__main__':
	n = int(input())
	R = list(map(str, input().split()))
	C = R[:]
	SR = selectionSort(R, n)
	BR = bubbleSort(C, n)

	fStable = SR == BR

	print(" ".join(map(str, BR)))
	print("Stable")
	print(" ".join(map(str, SR)))
	if (fStable == True):
		print("Stable")
	else:
		print("Not stable")