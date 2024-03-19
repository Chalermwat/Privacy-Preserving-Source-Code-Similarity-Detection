#!/usr/bin/env python3
import sys
class mystack:
  v = [0 for i in range(222)]
  t = 0

  def push(self,a):
    self.t += 1
    self.v[self.t] = a
  def pop(self):
    self.t -= 1
  def top(self):
    return self.v[self.t]
  def pr(self):
    for i in range(1, self.t+1):
      sys.stdout.write(self.v[i] + " ")
    sys.stdout.write('\n')

s = mystack()
l = sys.stdin.readline().split()

for i in l:
  if not i.isdigit():
    a = s.top()
    s.pop()
    b = s.top()
    s.pop()
    if i == '+':
      s.push(b+a)
    if i == '-':
      s.push(b-a)
    if i == '*':
      s.push(b*a)
  else:
    s.push(int(i))

print(s.top())