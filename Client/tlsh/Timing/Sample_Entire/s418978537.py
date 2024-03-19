from collections import deque

data = input()
tmp = deque()
se = list()
ase = list()
lakes = list()

x = 0
#check start - end
for a in data:
  if a == '\\':
    tmp.append(x)
  if a == '/' and len(tmp) > 0 :
    s = tmp.pop()
    se.append([s,x])
  x += 1
se.sort()

# analyse s -e
if len(se) > 0 :
  ase.append(se[0])
  for i in range(1,len(se)) :
    s,e = ase[len(ase)-1]
    if e < se[i][0]:
      ase.append(se[i])

#calc lakes
for a in ase:
  lsize = 0
  deep = 0
  lx = a[0]
  for m in data[a[0]:a[1] + 1] :
    if m == '\\':
      lsize += 1 + deep
      deep += 1
    elif m == '/':
      deep -= 1
      lsize += deep
      if lx == a[1]:
        lakes.append(lsize)
    else: # '_'
      lsize += deep
    lx += 1

print(sum(lakes))
print(len(lakes),end="")
for lake in lakes:
  print(" {}".format(lake),end="")
print()
