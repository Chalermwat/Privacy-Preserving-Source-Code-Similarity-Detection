#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re

def embedded_numbers(str):
	re_digits = re.compile(r'(\d+)')
	pieces = re_digits.split(str)
	pieces[1] = map(int, pieces[1])
	return pieces[1]

def selectionSort(Arry):
	for i in range(len(Arry)):
		minj = i
		for j in range(i,len(Arry)):
			if embedded_numbers(Arry[j]) < embedded_numbers(Arry[minj]):
				minj = j
		Arry[i],Arry[minj] = Arry[minj], Arry[i]

	return Arry

def bubbleSort(Arry):
	for i in range(len(Arry)):
		for j in range(len(Arry) - 1, i, -1):
			if embedded_numbers(Arry[j-1]) > embedded_numbers(Arry[j]):
				Arry[j-1], Arry[j] = Arry[j], Arry[j - 1]
	
	return Arry

def judge_satble(origin, sortedCards):
	if sorted(origin, key=embedded_numbers) == sortedCards:
		print "Stable"
	else:
		print "Not stable"

def main():
	
	N = int(raw_input())
	Cards = raw_input().split()
	s_cards = list(Cards)
	b_cards = list(Cards)
	
	bubble_sortedCards = bubbleSort(b_cards)
	print " ".join(bubble_sortedCards)
	judge_satble(Cards, bubble_sortedCards)

	select_sortedCards = selectionSort(s_cards)
	print " ".join(select_sortedCards)
	judge_satble(Cards, select_sortedCards)


#def test():
	#if  1 > embedded_numbers("s8"):
		#print "ok"


	
if __name__ == '__main__':
	main()
	#test()