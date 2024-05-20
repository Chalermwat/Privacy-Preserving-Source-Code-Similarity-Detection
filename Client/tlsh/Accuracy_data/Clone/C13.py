#!usr/bin/env python3
from collections import defaultdict ,deque #line:2
from heapq import heappush ,heappop #line:3
from itertools import permutations ,accumulate #line:4
import sys #line:5
import math #line:6
import bisect #line:7
def LI ():return [int (OO0OOOOOO000O00O0 )for OO0OOOOOO000O00O0 in sys .stdin .buffer .readline ().split ()]#line:8
def I ():return int (sys .stdin .buffer .readline ())#line:9
def LS ():return [list (OOO0000O000OOOO0O )for OOO0000O000OOOO0O in sys .stdin .readline ().split ()]#line:10
def S ():#line:11
    O000O000OOO000000 =list (sys .stdin .readline ())#line:12
    if O000O000OOO000000 [-1 ]=="\n":#line:13
        return O000O000OOO000000 [:-1 ]#line:14
    return O000O000OOO000000 #line:15
def IR (OO0O00OO00OO0O000 ):#line:16
    return [I ()for O000O0O00O0000O00 in range (OO0O00OO00OO0O000 )]#line:17
def LIR (OO0O00O000OOOO000 ):#line:18
    return [LI ()for OO00O000OOO0OO0OO in range (OO0O00O000OOOO000 )]#line:19
def SR (O0000OO00O0O0OOO0 ):#line:20
    return [S ()for O00OOOO0OO0OOO0OO in range (O0000OO00O0O0OOO0 )]#line:21
def LSR (OOOOOO000000OO0O0 ):#line:22
    return [LS ()for O0O0O0OO000OOOOO0 in range (OOOOOO000000OO0O0 )]#line:23
sys .setrecursionlimit (1000000 )#line:25
mod =1000000007 #line:26
def solve ():#line:28
    O00OOO00OOOO0OOOO =I ()#line:29
    OOOO0000OOOO00OOO =LI ()#line:30
    O00O0O0O0O0OOO0O0 =[2 if OOO0OO0O0OOO000OO &1 else 1 for OOO0OO0O0OOO000OO in OOOO0000OOOO00OOO ]#line:31
    OO0O0O000O0OO000O =0 #line:32
    for OOOOO00O0OO000OOO in range ((1 <<O00OOO00OOOO0OOOO )-1 ):#line:33
        O0OO0O0OOOO000000 =1 #line:34
        for O0OOOOOO0OOO0O00O in range (O00OOO00OOOO0OOOO ):#line:35
            O0OO0O0OOOO000000 *=(O00O0O0O0O0OOO0O0 [O0OOOOOO0OOO0O00O ]<<(OOOOO00O0OO000OOO >>O0OOOOOO0OOO0O00O ))%3 #line:36
        OO0O0O000O0OO000O +=O0OO0O0OOOO000000 #line:37
    print (OO0O0O000O0OO000O )#line:38
    return #line:39
if __name__ =="__main__":#line:42
    solve ()#line:43
