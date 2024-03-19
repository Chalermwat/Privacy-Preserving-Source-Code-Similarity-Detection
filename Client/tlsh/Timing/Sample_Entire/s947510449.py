s = input()
highest, high, h, mh = [0], [0], 0, 0
for i in range(len(s)):
    if s[-i-1] == '\\':     h += 1
    elif s[-i-1] == "/":    h -= 1
    
    if mh < h:  mh = h
    
    high.append(h)
    highest.append(mh)

high, highest = high[::-1], highest[::-1]
puddle, h = [], high[0]
v, vsum = 0, 0
for i in range(1, len(s) + 1):
    h = min(h, highest[i])
    if high[i] < h:
        if s[i-1] != "_":
            v -= 0.5
        v += h - min(high[i-1], high[i])
    elif v != 0:
        v = int(v + 0.5)
        puddle.append(v)
        vsum += v
        v, h = 0, high[i]
    else:
        h = high[i]
        
print(vsum)
if len(puddle) != 0:
    print(len(puddle), ' '.join(list(map(str, puddle))))
else:
    print(0)
