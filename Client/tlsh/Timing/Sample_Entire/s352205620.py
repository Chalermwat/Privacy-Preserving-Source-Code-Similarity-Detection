S = raw_input()

areas = []
stack = []
for i,c in enumerate(S):
    if c == "\\":
        stack.append(i)
    elif c == "/":
        if len(stack) > 0:
            j = stack.pop()
            area = i-j
            while len(areas) > 0:
                p,a = areas.pop()
                if j < p:
                    area += a
                else:
                    areas.append((p, a))
                    break
            areas.append((j, area))

A = map(lambda x:x[1], areas)
print sum(A)
if len(A) == 0:
    print "0"
else:
    print len(A), " ".join(map(str, A))
