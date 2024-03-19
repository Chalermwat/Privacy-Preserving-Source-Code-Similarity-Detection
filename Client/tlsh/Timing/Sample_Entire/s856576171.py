N = int(input())
SI = list(input().split())
SB = SI.copy()

# bubble sort
for i in range(N):
	for j in range(N - 1, i, -1):
		if SB[j - 1][1] > SB[j][1]:
			x = SB[j - 1]
			SB[j - 1] = SB[j]
			SB[j] = x

# insertion sort
for i in range(N):
	ptr = i
	for j in range(i + 1, N):
		if SI[ptr][1] > SI[j][1]:
			ptr = j
	x = SI[i]
	SI[i] = SI[ptr]
	SI[ptr] = x

# print the answer!
for i in range(N):
	print(SB[i] + " " if i != N - 1 else str(SB[i]) + "\n", end='')
print("Stable")
for i in range(N):
	print(SI[i] + " " if i != N - 1 else str(SI[i]) + "\n", end='')
print("Stable" if SI == SB else "Not stable")

