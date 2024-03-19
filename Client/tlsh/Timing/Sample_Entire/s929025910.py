# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 23:10:10 2018

@author: maezawa
"""

s = input()
n = len(s)

st = []
st2 = []
total_sum = 0

for i, c in enumerate(s):
    if c == '\\': # Back Slashをそのまま使うため二重にした。
        st.insert(0,i)
    elif c == '/' and len(st)>0: 
        j = st.pop(0)
        total_sum += i - j
        a = i - j
        while len(st2) > 0 and st2[0][0] > j:
            a += st2.pop(0)[1]
        st2.insert(0, [j, a])
        
print(total_sum)
print(len(st2), end='')
for i in reversed(range(len(st2))):
    print(" {}".format(st2[i][1]), end='')
print()



