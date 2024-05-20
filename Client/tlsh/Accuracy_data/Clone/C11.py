import sys ,os #line:1
from collections import defaultdict ,deque #line:2
from math import ceil ,floor #line:3
if sys .version_info [1 ]>=5 :#line:4
    from math import gcd #line:5
else :#line:6
    from fractions import gcd #line:7
sys .setrecursionlimit (10 **6 )#line:8
write =sys .stdout .write #line:9
dbg =(lambda *OOO0OO00O0O0O000O :print (*OOO0OO00O0O0O000O ))if 'TERM_PROGRAM'in os .environ else lambda *OOO00O0OOOO00OOO0 :0 #line:10
def main (given =sys .stdin .readline ):#line:11
    OOO0O0OOOO0O00000 =lambda :given ().rstrip ()#line:12
    OOO000OOO000OO0OO =lambda :list (map (int ,OOO0O0OOOO0O00000 ().split ()))#line:13
    OO0O00OO0O0O000O0 =lambda :int (OOO0O0OOOO0O00000 ())#line:14
    OO000OOOOOOO0OOO0 =998244353 #line:15
    O0OO00OOO00OOOOO0 =OO0O00OO0O0O000O0 ()#line:17
    O0O000OO0O0OO00O0 =OOO000OOO000OO0OO ()#line:18
    OOO0O0O00OOOO0000 =[0 ]*O0OO00OOO00OOOOO0 #line:19
    for O0OOO00OO0000O000 in O0O000OO0O0OO00O0 :#line:20
        OOO0O0O00OOOO0000 [O0OOO00OO0000O000 ]+=1 #line:21
    if O0O000OO0O0OO00O0 [0 ]!=0 or OOO0O0O00OOOO0000 [0 ]!=1 :#line:22
        print (0 )#line:23
        return #line:24
    O00OO0OOOOO0OO00O =1 #line:25
    OOO0O0000OO00OO00 =1 #line:26
    dbg (OOO0O0O00OOOO0000 )#line:27
    for OOOOOO00O00O0O0OO ,O0OOO0O0O0O0O0O0O in enumerate (OOO0O0O00OOOO0000 ):#line:28
        if O0OOO0O0O0O0O0O0O ==0 :#line:29
            if O0OO00OOO00OOOOO0 -OOOOOO00O00O0O0OO !=OOO0O0O00OOOO0000 .count (0 ):#line:30
                print (0 )#line:31
                return #line:32
            break #line:33
        O00OO0OOOOO0OO00O *=pow (OOO0O0000OO00OO00 ,O0OOO0O0O0O0O0O0O ,OO000OOOOOOO0OOO0 )#line:34
        O00OO0OOOOO0OO00O %=OO000OOOOOOO0OOO0 #line:35
        OOO0O0000OO00OO00 =O0OOO0O0O0O0O0O0O #line:36
    print (O00OO0OOOOO0OO00O )#line:37
if __name__ =='__main__':#line:44
    main ()