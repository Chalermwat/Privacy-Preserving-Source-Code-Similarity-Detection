w = input()

h = [0]

for i in range(len(w)):
  if w[i] == "/":
    h.append(h[i]+1)
  elif w[i] == "_":
    h.append(h[i])
  else:
    h.append(h[i]-1)

L = []

lstart = []

for i in range(len(w)):
  if w[i] == "\\":
    lstart.append(i)
    L.append(0)
  elif w[i] == "/" and not lstart == []:
    j = lstart.pop()
    s = i-j
    for k in range(1, i-j):
      if L[i-k]>0:
        s += L.pop(i-k)
        L.append(0)
    L.append(s)
  else:
    L.append(0)

L = [i for i in L if i > 0]

print(sum(L))
L.insert(0,len(L))
print(" ".join(map(str, L)))
