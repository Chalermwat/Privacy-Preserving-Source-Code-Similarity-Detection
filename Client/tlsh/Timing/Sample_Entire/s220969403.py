#!/usr/bin/env python                                                                                                                   
inputlist = map(str,raw_input().split())
numberlist = []
for a in inputlist:
    if a == "+":
        b = numberlist[-2]
	c = numberlist[-1]
	numberlist[-2:]=[]
	d = int(b) + int(c)
	numberlist.append(d)
    elif a == "-":
        b = numberlist[-2]
        c = numberlist[-1]
        numberlist[-2:]=[]
        d = int(b) - int(c)
        numberlist.append(d)
    elif a == "*":
	b = numberlist[-2]
        c = numberlist[-1]
        numberlist[-2:]=[]
        d = int(b) * int(c)
	numberlist.append(d)
    else:
        numberlist.append(a)
print(numberlist[0])