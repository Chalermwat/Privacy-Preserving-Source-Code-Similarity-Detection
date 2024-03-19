import copy

n = int(raw_input())
cards = raw_input().split()
cards1 = copy.deepcopy(cards)
cards2 = copy.deepcopy(cards)

def isbig(card1, card2):
	if int(card1[1]) > int(card2[1]):
		return 2
	elif int(card1[1]) == int(card2[1]):
		return 1
	else:
		return 0

def BubbleSort(c, n):
	temp = 0
	for i in range(n):
		for j in reversed(range(i+1,n)):
			if isbig(c[j], c[j-1]) == 0:
				temp = c[j]
				c[j] = c[j-1]
				c[j-1] = temp
	return c

def SelectionSort(c, n):
	temp = 0
	for i in range(n):
		minj = i
		for j in range(i,n):
			if isbig(c[j], c[minj]) == 0:
				minj = j
		temp = c[i]
		c[i] = c[minj]
		c[minj] = temp
		#print("*{:}".format(c))
	return c

def isstable(unsort, sort):
	for i in range(n):
		for j in range(i+1,n):
			for k in range(n):
				for l in range(k+1,n):
					if isbig(unsort[i], unsort[j]) == 1 and unsort[i] == sort[l] and unsort[j] == sort[k]:
						return 0
	return 1

for i in range(n):
	if i != n-1:
		print BubbleSort(cards1, n)[i],
	else:
		print BubbleSort(cards1, n)[i]

if isstable(cards, BubbleSort(cards1, n)) == 1:
	print("Stable")
else:
	print("Not stable")

for i in range(n):
	if i != n-1:
		print SelectionSort(cards2, n)[i],
	else:
		print SelectionSort(cards2, n)[i]

if isstable(cards, SelectionSort(cards2, n)) == 1:
	print("Stable")
else:
	print("Not stable")