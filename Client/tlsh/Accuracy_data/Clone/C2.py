from sys import stdin #line:1
from collections import deque #line:2
N ,K =[int (OOO0OOOO00O00O000 )for OOO0OOOO00O00O000 in stdin .readline ().rstrip ().split ()]#line:3
V =[int (O0O0O0OO0OO0O0O0O )for O0O0O0OO0OO0O0O0O in stdin .readline ().rstrip ().split ()]#line:4
ans =0 #line:5
rev_V =V [::-1 ]#line:6
for L in range (0 ,K +1 ):#line:8
        for R in range (0 ,K +1 ):#line:9
            if L +R >min (K ,N ):#line:10
                break #line:11
            tmp =V [0 :L ]+rev_V [0 :R ]#line:13
            tmp .sort ()#line:14
            tmp =deque (tmp )#line:15
            num =K -(L +R )#line:16
            stone =-1 #line:17
            cnt =0 #line:18
            while stone <0 :#line:19
                if cnt >=num or len (tmp )==0 :#line:20
                    break #line:21
                stone =tmp .popleft ()#line:22
                if stone >=0 :#line:23
                    tmp .append (stone )#line:24
                    break #line:25
                cnt +=1 #line:26
            ans =max (ans ,sum (tmp ))#line:27
print (ans )