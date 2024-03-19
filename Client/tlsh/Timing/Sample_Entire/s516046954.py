def BubbleSort(lists, num):
  cards = lists[:]
  for i in xrange(num):
    for j in xrange(num - 1, i, -1):
      if cards[j].value < cards[j - 1].value:
        cards[j], cards[j - 1] = cards[j - 1], cards[j]
  return cards

def SelectionSort(lists, num):
  cards = lists[:]
  for i in xrange(num):
    minj = i
    for j in xrange(i, num):
      if cards[j].value < cards[minj].value:
        minj = j
    cards[i], cards[minj] = cards[minj], cards[i]
  return cards

class Card(object):
  """docstring for Card"""
  def __init__(self, arg):
    self.mark = arg[0]
    self.value = int(arg[1])

num = int(raw_input())
inputs = raw_input().split()
cards = [Card(inputs[x]) for x in xrange(num)]

bubble_ans = ""
bubble_cards = BubbleSort(cards, num)
for x in bubble_cards:
  bubble_ans += x.mark + str(x.value) + " "
print bubble_ans.rstrip()
print "Stable"

select_ans = ""
select_cards = SelectionSort(cards, num)
for x in select_cards:
  select_ans += x.mark + str(x.value) + " "
print select_ans.rstrip()
flag = True
for x in xrange(num):
  if bubble_cards[x].mark != select_cards[x].mark:
    flag = False
    break
print "Stable" if flag else "Not stable"