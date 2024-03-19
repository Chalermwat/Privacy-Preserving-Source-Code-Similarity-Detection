import sys

def isEmpty(S):
  if len(S) == 0:
    return True
  
def isFull(S):
  if len(S) >= 101:
    return True

def push(x):
  if isFull(S):
    print 'Error'
  S.append(x)
  
def pop(top):
  if isEmpty(S):
    print 'error'
  k = S[top]
  S.pop()
  return k

S = []
top = -1

x = sys.stdin.readline().strip()
x_list = x.split(" ")

for i in range(0, len(x_list)):
  if x_list[i] == '*':
    a = int(pop(top))
    top -= 1
    b = int(pop(top))
    top -= 1
    push(a * b)
    top += 1
    
  elif x_list[i] == '+':
    a = int(pop(top))
    top -= 1
    b = int(pop(top))
    top -= 1
    push(a + b)
    top += 1
    
  elif x_list[i] == '-':
    a = int(pop(top))
    top -= 1
    b = int(pop(top))
    top -= 1
    push(b - a)
    top += 1
    
  else:
    push(x_list[i])
    top += 1
    
a = int(pop(top))
print a