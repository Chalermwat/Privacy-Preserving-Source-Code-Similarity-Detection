#coding: UTF-8

import copy
class Algo:
  @staticmethod
  def bubbleSort(r, c, n):
    flag = 1
    while flag:
      flag = 0
      for j in range(n-1, 0, -1):
        if c[j] < c[j-1]:
          c[j], c[j-1] = c[j-1], c[j]
          r[j], r[j-1] = r[j-1], r[j]
          flag = 1
    return r

  def selectionSort(r, c, n):
    for i in range(0,n):
      minj = i
      for j in range(i,n):
        if c[j] < c[minj]:
          minj = j
      if c[i] != c[minj]:
        c[i], c[minj] = c[minj], c[i]
        r[i], r[minj] = r[minj], r[i]
    return r

  def createIntList(r, n):
    c = []
    for i in range(0,n):
      c.append(r[i][1])
    return c

  def printList(r, n):
    for i in range(0,n):
      if i == n-1:
        print(r[i])
      else:
        print(r[i], " ", sep="", end="")

n = int(input())
r = list(map(str,input().split()))
c = Algo.createIntList(r, n)
br = Algo.bubbleSort(copy.deepcopy(r), copy.deepcopy(c), n)
ir = Algo.selectionSort(copy.deepcopy(r), copy.deepcopy(c), n)
Algo.printList(br, n)
print("Stable")
Algo.printList(ir, n)
if br == ir:
  print("Stable")
else:
  print("Not stable")