class Sort():
	def __init__(self,n,cards):
		self.cards = cards
		self.n = n

	def bubble_sort(self):
		# bubble sort
		flag = 1
		while flag != 0:
			flag = 0
			rev = list(range(1,self.n))
			rev.reverse()
			for j in rev:
				if int(self.cards[j][1]) < int(self.cards[j-1][1]):
					self.cards[j],self.cards[j-1] = self.cards[j-1],self.cards[j]
					flag = 1

	def select_sort(self):
		for i in range(self.n):
			mini = i
			for j in range(i,self.n):
				if int(self.cards[j][1]) < int(self.cards[mini][1]):
					mini = j
			if i != mini:
				self.cards[i],self.cards[mini] = self.cards[mini],self.cards[i]

	def check_stable(self,origin):
		check_org = [["" for i in range(self.n)] for k in range(9)]
		check_sort = [["" for i in range(self.n)] for k in range(9)]
		for i in range(self.n):
			check_org[int(origin[i][1])-1][i] = origin[i][0]
			check_sort[int(self.cards[i][1])-1][i] = self.cards[i][0]
		flag = 0
		for i in range(9):
			if "".join(check_org[i]) != "".join(check_sort[i]):
				flag = 1
				break

		if flag == 0:
			print("Stable")
		else:
			print("Not stable")

	def print_card(self):
		for i in range(self.n):
			if i != self.n-1:
				print("%s" % (self.cards[i]),end=" ")
			else:
				print("%s" % (self.cards[i]))

if __name__ == '__main__':
	n = int(input())
	card = input().split()
	card2 = card.copy()
	card_origin = card.copy()
	
	bubble = Sort(n,card)
	bubble.bubble_sort()
	bubble.print_card()
	bubble.check_stable(card_origin)
	
	select = Sort(n,card2)
	select.select_sort()
	select.print_card()
	select.check_stable(card_origin)
